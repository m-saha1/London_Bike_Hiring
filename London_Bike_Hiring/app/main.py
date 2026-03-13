from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app import crud, analytics

from ml import demand_model
from ml import shock_detection

app = FastAPI(title="London Bike Analysis")


@app.get("/")
def root():
    return {"message": "London Bike Analysis API"}


@app.get("/journeys")
def journeys(db: Session = Depends(get_db)):
    return crud.get_journeys(db)


@app.get("/routes")
def routes(db: Session = Depends(get_db)):
    return crud.get_top_routes(db)


@app.get("/ml/demand")
def train_model():

    df = analytics.load_dataframe(engine)

    demand = analytics.station_demand(df)

    model, rmse = demand_model.train_model(demand)

    return {"rmse": rmse}


@app.get("/ml/shocks")
def shocks():

    df = analytics.load_dataframe(engine)

    demand = analytics.station_demand(df)

    shocks = shock_detection.detect_shocks(demand)

    return shocks.head(10).to_dict()