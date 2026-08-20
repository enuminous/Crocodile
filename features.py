import numpy as np
import pandas as pd

def add_lagged_treatment(df, treatment_column, lags=(0,1,2,3,5,8,13,21)):
    out=pd.DataFrame(index=df.index)
    t=df[treatment_column].astype(float)
    for lag in lags:
        out[f"treatment_lag_{lag}"]=t.shift(lag).fillna(0.0)
    return out

def downstream_features(df, downstream_columns, horizons=(3,7,23)):
    x=df[downstream_columns].astype(float).ffill().fillna(0.0)
    out=pd.DataFrame(index=df.index)
    for c in downstream_columns:
        out[c]=x[c]
        out[f"{c}__dx"]=x[c].diff().fillna(0.0)
        for h in horizons:
            out[f"{c}__mean_{h}"]=x[c].rolling(h,min_periods=1).mean()
    return out
