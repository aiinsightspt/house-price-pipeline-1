"""Tests on the data: a broken file must stop the pipeline before training."""
import pandas as pd

data = pd.read_csv("data/houses.csv")


def test_expected_columns():
    assert list(data.columns) == ["size_m2", "rooms", "age_years", "price_k_eur"]


def test_no_missing_values():
    assert data.notna().all().all()


def test_values_are_possible():
    assert (data["size_m2"] > 0).all()
    assert data["rooms"].between(1, 10).all()
    assert (data["age_years"] >= 0).all()
    assert (data["price_k_eur"] > 0).all()
