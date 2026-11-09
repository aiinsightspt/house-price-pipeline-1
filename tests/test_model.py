"""Tests on the model: its answers must make sense to a person."""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data/houses.csv")
FEATURES = ["size_m2", "rooms", "age_years"]
model = LinearRegression().fit(data[FEATURES], data["price_k_eur"])


def price(size, rooms, age):
    house = pd.DataFrame([[size, rooms, age]], columns=FEATURES)
    return model.predict(house)[0]


def test_typical_house_has_a_plausible_price():
    assert 150 < price(100, 3, 15) < 400


def test_bigger_house_costs_more():
    assert price(150, 3, 15) > price(100, 3, 15)


def test_older_house_costs_less():
    assert price(100, 3, 40) < price(100, 3, 5)
