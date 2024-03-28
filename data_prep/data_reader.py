import pandas as pd


def from_csv(path: str) -> pd.Dataframe:
    return pd.read_csv(path)


def from_excel(path: str) -> pd.Dataframe:
    return pd.read_excel(path)


def from_json(path: str) -> pd.DataFrame:
    return pd.read_json(path)