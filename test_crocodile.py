import pandas as pd
from crocodile import CROCODILEExperiment

def make_exp():
    return CROCODILEExperiment(
        time_column="time",
        treatment_column="treatment",
        outcome_column="outcome",
        post_column="post",
        downstream_columns=["downstream_a","downstream_b"],
    )

def test_run():
    df=pd.read_csv("example_data.csv")
    out=make_exp().run(df)
    assert "raw_average_treatment_effect" in out
    assert "difference_in_differences" in out
    assert "lag_effect_profile" in out
    assert "placebo_average_treatment_effect" in out

def test_lag_profile_contains_requested_lags():
    df=pd.read_csv("example_data.csv")
    out=make_exp().run(df)
    assert set(out["lag_effect_profile"].keys())=={"0","1","2","3","5","8","13","21"}

def test_placebo_is_reported_separately():
    df=pd.read_csv("example_data.csv")
    out=make_exp().run(df)
    assert out["placebo_shift"]==23
