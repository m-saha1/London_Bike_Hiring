import matplotlib.pyplot as plt

from app.database import engine
from app.analytics import load_dataframe
from ml.shock_detection import detect_shocks


print("Loading bike data from database...")

df = load_dataframe(engine)

print("Detecting shocks...")

shocks = detect_shocks(df)

normal = shocks[shocks["anomaly"] == 1]
anomaly = shocks[shocks["anomaly"] == -1]


plt.figure(figsize=(14,6))

plt.plot(
    shocks["hour"],
    shocks["trips"],
    label="Normal Demand"
)

plt.scatter(
    anomaly["hour"],
    anomaly["trips"],
    label="Demand Shock",
    s=80
)

plt.title("Bike Network Demand Shocks Over Time")

plt.xlabel("Time")
plt.ylabel("Trips per Hour")

plt.legend()

plt.tight_layout()

plt.show()