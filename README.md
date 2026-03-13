# London Bike Network Analysis

A personal data science project analysing the **London Cycle Hire network** using Python, PostgreSQL, and machine learning.

This project investigates how bike demand behaves across the city and how the system responds to unusual demand spikes.

---

# Project Goals

This analysis explores three key questions:

### Where are the bikes going?

Bike journey data is aggregated into **station-to-station flows** to understand movement patterns across London.

### What is the cost of prediction errors?

A demand forecasting model estimates hourly bike usage.
Prediction accuracy is measured using **RMSE (Root Mean Square Error)**.

### How does the network handle severe demand shocks?

An **Isolation Forest anomaly detection model** identifies unusual spikes in bike demand.

---

# Dataset

The dataset comes from **Transport for London's Cycle Hire open data**.

Each journey record contains:

* start station
* end station
* start time
* duration
* bike ID

The data is stored in a **PostgreSQL database** and analysed using Python.

Dataset source:

https://cycling.data.tfl.gov.uk/

---

# Machine Learning Models

## Demand Forecasting Model

Predicts hourly demand using features such as:

* hour of day
* day of week

Evaluation metric:

```
RMSE ≈ 11 trips/hour
```

This means predictions typically deviate by around **11 trips per hour**.

---

## Demand Shock Detection

Demand anomalies are detected using **Isolation Forest**.

The contamination parameter was tuned to:

```
1%
```

This isolates the most extreme demand spikes across the network.

---

# Example Output

The model identifies periods of unusually high bike usage across London.

Example demand shock visualisation:

```
<img width="1400" height="600" alt="Demand_Shock_Example" src="https://github.com/user-attachments/assets/dd1071e0-75ce-4813-9f44-9e008360f6ef" />

```

---

# Technologies Used

Python
PostgreSQL
SQLAlchemy
Pandas
NumPy
Scikit-learn
Matplotlib

---

# Project Structure

```
london-bike-analysis
│
├── app
│   ├── database.py
│   ├── analytics.py
|   ├── crud.py
|   ├── main.py
|   ├── models.py
|   ├── schema.py
|   └── run_analytics.py
│
├── ml
│   ├── demand_model.py
│   └── shock_detection.py
│
├── visualisations
│   └── plot.py
│
├── requirements.txt
├── README.md
└── .env_example
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/london-bike-analysis
```

Move into the project:

```
cd london-bike-analysis
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file using the template:

```
cp .env.example .env
```

Then update with your PostgreSQL credentials.

---

# Running the Project

Example analysis:

```
python visualisations/plot.py
```

This will load the data from PostgreSQL and generate demand shock visualisations.

---

# Future Improvements

Potential extensions:

* station-level demand forecasting
* network flow visualisation
* interactive dashboards
* weather impact analysis
* real-time analytics API

---

# 👤 Author

Mohamed Sahal a 2nd Year Data Science & AI at UAL's Creative Computing Institute (CCI)

Personal data science project exploring **urban mobility and transport analytics**.
