import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_shocks(df):
    """
    Detect demand shocks in the bike network using Isolation Forest.
    """

    # Ensure datetime format
    df["start_date"] = pd.to_datetime(df["start_date"])

    # Create hourly timestamp
    df["hour"] = df["start_date"].dt.floor("h")

    # Aggregate trips per hour
    hourly = (
        df.groupby("hour")
        .size()
        .reset_index(name="trips")
        .sort_values("hour")
    )

    # Feature engineering
    hourly["hour_of_day"] = hourly["hour"].dt.hour
    hourly["day_of_week"] = hourly["hour"].dt.dayofweek

    features = hourly[["trips", "hour_of_day", "day_of_week"]]

    # Train anomaly detection model
    model = IsolationForest(
        n_estimators=200,
        contamination=0.01,
        random_state=42
    )

    hourly["anomaly"] = model.fit_predict(features)

    return hourly