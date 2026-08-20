import json
import pandas as pd
from crocodile import CROCODILEExperiment

df=pd.read_csv("example_data.csv")

exp=CROCODILEExperiment(
    time_column="time",
    treatment_column="treatment",
    outcome_column="outcome",
    post_column="post",
    downstream_columns=["downstream_a","downstream_b"],
    lags=(0,1,2,3,5,8,13,21),
    horizons=(3,7,23),
    placebo_shift=23,
)

print(json.dumps(exp.run(df),indent=2))
