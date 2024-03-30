import pandas as pd
from DataPrepKit.data_reader import from_csv, from_excel, from_json


def test_from_csv(path: str) -> pd.DataFrame:
    return from_csv(path)


df = test_from_csv("winemag-data-130k-v2.csv")
print(df.head())


def test_from_excel(path: str) -> pd.DataFrame:
    return from_excel(path)


df = test_from_excel("winemag-data-130k-v2.xlsx")
print(df.head())


def test_from_json(path: str) -> pd.DataFrame:
    return from_json(path)


df = test_from_json("iris.json")
print(df.head())
