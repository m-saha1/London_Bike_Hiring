import pandas as pd


def load_dataframe(engine):

    query = """
    SELECT
        start_date,
        start_station,
        end_station,
        total_duration
    FROM cycle_journeys
    WHERE start_date >= '2025-01-01'
    """

    df = pd.read_sql(query, engine)

    df["start_date"] = pd.to_datetime(df["start_date"])

    df["hour"] = df["start_date"].dt.hour
    df["day_of_week"] = df["start_date"].dt.dayofweek

    return df


def station_demand(df):

    demand = df.groupby(
        ["start_station", "hour"]
    ).size().reset_index(name="trip_count")

    return demand


def route_flows(df):

    routes = (
        df.groupby(["start_station","end_station"])
        .size()
        .reset_index(name="trips")
        .sort_values("trips", ascending=False)
    )

    return routes