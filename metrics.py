import numpy as np

def ate(y,t):
    y=np.asarray(y,dtype=float)
    t=np.asarray(t,dtype=int)
    if not ((t==1).any() and (t==0).any()):
        return None
    return float(y[t==1].mean()-y[t==0].mean())

def did(df, outcome_column, treatment_column, post_column):
    treated=df[treatment_column].astype(int)==1
    control=~treated
    post=df[post_column].astype(int)==1
    pre=~post

    cells = [
        treated & post,
        treated & pre,
        control & post,
        control & pre,
    ]
    if not all(mask.any() for mask in cells):
        return None

    y=df[outcome_column].astype(float)
    treated_change=y[treated & post].mean()-y[treated & pre].mean()
    control_change=y[control & post].mean()-y[control & pre].mean()
    value=float(treated_change-control_change)
    return value if np.isfinite(value) else None

def lag_effects(df, outcome_column, treatment_column, lags):
    y=df[outcome_column].astype(float)
    t=df[treatment_column].astype(float)
    out={}
    for lag in lags:
        shifted=t.shift(lag).fillna(0.0)
        mask=(shifted==1)|(shifted==0)
        yy=y[mask]
        tt=shifted[mask].astype(int)
        out[str(lag)]=ate(yy,tt)
    return out
