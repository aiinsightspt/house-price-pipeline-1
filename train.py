"""Train the house-price model and measure it on houses it has not seen."""
import json

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

FEATURES = ["size_m2", "rooms", "age_years"]
TARGET = "price_k_eur"

# 1 · Read the data and keep 20% of the houses aside for the test.
data = pd.read_csv("data/houses.csv")
X_train, X_test, y_train, y_test = train_test_split(
    data[FEATURES], data[TARGET], test_size=0.2, random_state=42
)

# 2 · Train the model on the other 80%.
model = LinearRegression().fit(X_train, y_train)

# 3 · Measure the error on the test houses, and the error of a baseline
#     that ignores the inputs and always predicts the average price.
mae = mean_absolute_error(y_test, model.predict(X_test))
baseline_mae = mean_absolute_error(y_test, [y_train.mean()] * len(y_test))

# 4 · Save the model and its metrics: the next step reads them.
joblib.dump(model, "model.joblib")
metrics = {"mae": round(mae, 1), "baseline_mae": round(baseline_mae, 1),
           "test_houses": len(y_test)}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(metrics)
