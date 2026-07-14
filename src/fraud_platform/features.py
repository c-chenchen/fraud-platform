import pandas as pd


def add_time_features(df: pd.DataFrame, ts_col: str = "TransactionDT") -> pd.DataFrame:
    """Derive hour-of-day and day-of-week from the transaction timestamp.

    IEEE-CIS gives TranscactionDT as seconds from a reference point,
    not a real datetime, so we work in seconds directly.
    """

    out = df.copy()
    out["hour_of_day"] = (out[ts_col] // 3600) % 24
    out["day_of_week"] = (out[ts_col] // 86400) % 7
    return out
