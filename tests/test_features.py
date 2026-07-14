import pandas as pd

from fraud_platform.features import add_time_features


def test_hour_of_day_wraps_at_24():
    df = pd.DataFrame({"TransactionDT": [0, 3600, 86400 + 7200]})
    out = add_time_features(df)
    assert out["hour_of_day"].tolist() == [0, 1, 2]


def test_original_frame_not_mutated():
    df = pd.DataFrame({"TransactionDT": [0]})
    add_time_features(df)
    assert list(df.columns) == ["TransactionDT"]
