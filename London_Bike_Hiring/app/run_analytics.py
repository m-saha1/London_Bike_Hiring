from app.database import engine
from app import analytics
from ml import demand_model
from ml import shock_detection


print("Loading data from database...")

df = analytics.load_dataframe(engine)

print("Rows:", len(df))

print("\nTop routes:")
print(analytics.route_flows(df))

print("\nStation demand sample:")
demand = analytics.station_demand(df)

print(demand.head())

print("\nTraining ML model...")
model, rmse = demand_model.train_model(demand)

print("RMSE:", rmse)

print("\nDetecting shocks...")
shocks = shock_detection.detect_shocks(demand)

print(shocks.head())