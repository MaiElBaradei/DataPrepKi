import pandas as pd
from typing import Union


def from_csv(path: str) -> Union[pd.DataFrame, None]:
    """
    Read a comma-separated values (csv) file into DataFrame.

    Also supports optionally iterating or breaking of the file into chunks.

    Parameters:
    path: filepath_or_bufferstr, path object or file-like object
    Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is expected. 
    A local file could be: file://localhost/path/to/table.csv.

    If you want to pass in a path object, pandas accepts any os.PathLike.

    By file-like object, we refer to objects with a read() method, such as a file handle (e.g. via builtin open function) or StringIO.
    """

    try:
        return pd.read_csv(path)
    except ExceptionType as e:
        print(f"Error reading CSV file: {e}")


def from_excel(path: str) -> Union[pd.DataFrame, None]:
    """
    Read an Excel file into a pandas DataFrame.

    Supports xls, xlsx, xlsm, xlsb, odf, ods and odt file extensions read from a local filesystem or URL. Supports an option to read a single sheet or a list of sheets.

    Parameters:
    path: str, bytes, ExcelFile, xlrd.Book, path object, or file-like object
    Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. 
    A local file could be: file://localhost/path/to/table.xlsx.

    If you want to pass in a path object, pandas accepts any os.PathLike.

    By file-like object, we refer to objects with a read() method, such as a file handle (e.g. via builtin open function) or StringIO.
    """
    try:
        return pd.read_excel(path)
    except ExceptionType as e:
        print(f"Error reading Excel file: {e}")


def from_json(path: str) -> Union[pd.DataFrame, None]:
    """
    Convert a JSON string to pandas object.

    Parameters:
    path: a valid JSON str, path object or file-like object
    Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. 
    A local file could be: file://localhost/path/to/table.json.

    If you want to pass in a path object, pandas accepts any os.PathLike.

    By file-like object, we refer to objects with a read() method, such as a file handle (e.g. via builtin open function) or StringIO.
    """

    try:
        return pd.read_json(path)
    except ExceptionType as e:
        print(f"Error reading JSON file: {e}")
