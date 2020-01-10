"""
Base pandas functionality. `pd.FUNCTIONS`.
"""
import pandas as pd

from ..base import Pipeable, unpack_input, append_docstring


@unpack_input
@Pipeable
@append_docstring(pd.merge)
def Merge(*args, unpack_input=True, **kwargs):
    """
    Implements `pd.merge()`.

    :param *args:
        Any args accepted by `pd.merge()`.
    :param **kwargs:
        Any kwargs accepted by `pd.merge()`.

    """
    merged = pd.merge(*args, **kwargs)
    return merged


@Pipeable
@append_docstring(pd.read_csv)
def ReadCSV(*args, **kwargs):
    """
    Implements `pd.read_csv()`.

    :param *args:
        Any args accepted by `pd.read_csv()`.
    :param **kwargs:
        Any kwargs accepted by `pd.read_csv()`.

    """
    return pd.read_csv(*args, **kwargs)


@Pipeable
@append_docstring(pd.to_datetime)
def ToDatetime(df, *args, **kwargs):
    """
    Implements `pd.to_datetime()`.

    :param *args:
        Any args accepted by `pd.to_datetime()`.
    :param **kwargs:
        Any kwargs accepted by `pd.to_datetime()`.

    """
    if not args:
        df = pd.to_datetime(df)
    else:
        for column in args:
            df[column] = pd.to_datetime(df[column], **kwargs)
    return df

