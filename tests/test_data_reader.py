import pandas as pd
import pytest
from DataPrepKit.data_reader import from_csv, from_excel, from_json


def test_from_csv():
    df = from_csv("DataPrepKit/winemag-data-130k-v2.csv")
    assert isinstance(df, pd.DataFrame)


def test_from_excel():
    df = from_excel("DataPrepKit/winemag-data-130k-v2.xlsx")
    assert isinstance(df, pd.DataFrame)


def test_from_json():
    df = from_json("DataPrepKit/iris.json")
    assert isinstance(df, pd.DataFrame)
