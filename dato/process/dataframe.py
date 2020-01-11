"""
pandas.DataFrame processing functions.
"""
import pandas as pd

from ..base import Pipeable, unpack_input, append_docstring


@Pipeable
@append_docstring(pd.DataFrame.drop)
def Drop(df, *args, axis=1, **kwargs):
    """
    Implements `pd.DataFrame.drop()`, changing the default behavior to drop columns, not rows.

    :param *args:
        Any args accepted by `pd.DataFrame.drop`.
    :param **kwargs:
        Any kwargs accepted by `pd.DataFrame.drop()`.

    """
    return df.drop(*args, axis=axis, **kwargs)


@Pipeable
@append_docstring(pd.DataFrame.dropna)
def DropNA(df, *args, **kwargs):
    """
    Implements `pd.DataFrame.dropna()`.

    :param *args:
        Any args accepted by `pd.DataFrame.dropna`.
    :param **kwargs:
        Any kwargs accepted by `pd.DataFrame.dropna()`.

    """
    return df.dropna(*args, **kwargs)



@Pipeable
@append_docstring(pd.DataFrame.fillna)
def FillNA(df, value=None, columns=None, **kwargs):
    """
    Implements `pd.DataFrame.fillna()`. If a scalar value is passed it is used to fill all missing values. Alternatively, an array-like 'value' can be given. It's expected that the array-like have the same length as 'self'.

    :param value: the value used to fill
    :type value: scalar, array-like
    :param columns: columns to apply fillna to
    :type columns: array-like
    :param **kwargs:
        Anything accepted by the `pd.DataFrame.fillna()` method.

    """
    df1 = df.copy()
    if columns is not None:
        for column in columns:
            df1[column] = df1[column].fillna(value=value, **kwargs)
    else:
        df1 = df1.fillna(value=value, **kwargs)
    return df1


@Pipeable
@append_docstring(pd.DataFrame.groupby)
def GroupBy(df, *args, **kwargs):
    """
    Implements `pd.DataFrame.groupby()`.

    :param *args:
        Any args accepted by `pd.DataFrame.groupby()`.
    :param **kwargs:
        Any kwargs accepted by `pd.DataFrame.groupby()`.


    """
    gb = df.groupby(*args, **kwargs)
    return gb


@Pipeable
@append_docstring(pd.DataFrame.head)
def Head(df, *args, **kwargs):
    """
    Implements `pd.DataFrame.head()` (args and kwargs are passed through).

    """
    return df.head(*args, **kwargs)


@Pipeable
@append_docstring(pd.DataFrame.rename)
def Rename(df, *args, axis=1, **kwargs):
    """
    Implements pandas.DataFrame.rename, changing the default behavior to rename columns.
    """
    return df.rename(*args, axis=axis, **kwargs)


@Pipeable
@append_docstring(pd.DataFrame.sample)
def Sample(df, **kwargs):
    """
    Implements `df.sample()`.

    :param *args:
        Any args accepted by `df.sample()`.
    :param **kwargs:
        Any kwargs accepted by `df.sample()`.

    """
    return df.sample(**kwargs)


@Pipeable
def Select(df, *args):
    """
    Selects columns specified by args.

    :param *args: Column name.
    :type *args: tuple of strings.

    """
    return df[list(args)]


@Pipeable
@append_docstring(pd.DataFrame.sort_values)
def SortValues(df, *args, **kwargs):
    """
    Implements `df.sort_values()`.

    :param *args:
        Any args accepted by `df.sort_values()`.
    :param **kwargs:
        Any kwargs accepted by `df.sort_values()`.

    """
    return df.sort_values(*args, **kwargs)


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

