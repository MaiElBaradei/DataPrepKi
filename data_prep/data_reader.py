import pandas as pd
from typing import Union


def from_csv(path: str) -> Union[pd.Dataframe, None]:
    try:
        return pd.read_csv(path)
    except ExceptionType as e:
        print(f"Error reading CSV file: {e}")


def from_excel(path: str) -> Union[pd.Dataframe, None]:
    try:
        return pd.read_excel(path)
    except ExceptionType as e:
        print(f"Error reading EXcel file: {e}")


def from_json(path: str) -> Union[pd.Dataframe, None]:
    try:
        return pd.read_json(path)
    except ExceptionType as e:
        print(f"Error reading CSV file: {e}")
