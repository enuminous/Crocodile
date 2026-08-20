from dataclasses import dataclass
import numpy as np
import pandas as pd

from features import add_lagged_treatment, downstream_features
from metrics import ate, did, lag_effects
from models import LinearEffectModel

@dataclass
class CROCODILEExperiment:
    time_column: str
    treatment_column: str
    outcome_column: str
    post_column: str
    downstream_columns: list
    lags: tuple=(0,1,2,3,5,8,13,21)
    horizons: tuple=(3,7,23)
    placebo_shift: int=23

    def run(self,df):
        df=df.sort_values(self.time_column).reset_index(drop=True).copy()

        treatment=df[self.treatment_column].astype(int).to_numpy()
        outcome=df[self.outcome_column].astype(float).to_numpy()

        raw_ate=ate(outcome,treatment)
        did_est=did(df,self.outcome_column,self.treatment_column,self.post_column)
        lag_profile=lag_effects(df,self.outcome_column,self.treatment_column,self.lags)

        # placebo timing: shift treatment forward, preserving count but breaking true timing
        placebo=df.copy()
        placebo[self.treatment_column]=df[self.treatment_column].shift(self.placebo_shift).fillna(0).astype(int)
        placebo_ate=ate(
            placebo[self.outcome_column].to_numpy(),
            placebo[self.treatment_column].to_numpy()
        )

        # Downstream regression with lagged treatment and observed downstream state.
        lagged=add_lagged_treatment(df,self.treatment_column,self.lags)
        down=downstream_features(df,self.downstream_columns,self.horizons)
        X=pd.concat([lagged,down],axis=1).fillna(0.0)
        y=df[self.outcome_column].astype(float)

        model=LinearEffectModel().fit(X,y)
        coefs=dict(zip(X.columns,model.model.coef_))

        treatment_coefs={
            k:float(v) for k,v in coefs.items() if k.startswith("treatment_lag_")
        }

        # Pretrend check: compare treated vs control slope during pre-period.
        pre=df[self.post_column].astype(int)==0
        pre_df=df.loc[pre].copy()
        pretrend=None
        if len(pre_df)>=4 and pre_df[self.treatment_column].nunique()>1:
            slopes={}
            for group in [0,1]:
                g=pre_df[pre_df[self.treatment_column]==group]
                if len(g)>=2:
                    tt=g[self.time_column].astype(float).to_numpy()
                    yy=g[self.outcome_column].astype(float).to_numpy()
                    slope=np.polyfit(tt,yy,1)[0]
                    slopes[group]=float(slope)
            if 0 in slopes and 1 in slopes:
                pretrend=float(slopes[1]-slopes[0])

        return {
            "n_total":len(df),
            "raw_average_treatment_effect":raw_ate,
            "difference_in_differences":did_est,
            "lag_effect_profile":lag_profile,
            "placebo_shift":self.placebo_shift,
            "placebo_average_treatment_effect":placebo_ate,
            "pretrend_slope_difference":pretrend,
            "treatment_lag_coefficients":treatment_coefs,
            "interpretation":(
                "Causal interpretation requires a valid identification design. "
                "A large effect with poor pretrends or a similar placebo effect should not be treated as causal."
            )
        }
