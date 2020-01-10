"""
Matplotlib plotting functions.
"""
import pandas as pd

from ..base import Pipeable, unpack_input, append_docstring


@Pipeable
@append_docstring(pd.core.groupby.generic.DataFrameGroupBy.sum)
def Mean(gb, column=None, **kwargs):
    """
    Implements `pandas.core.groupby.generic.DataFrameGroupBy.mean()`.

    :param *args:
        Any args accepted by `pandas.core.groupby.generic.DataFrameGroupBy.mean()`.
    :param **kwargs:
        Any kwargs accepted by `pandas.core.groupby.generic.DataFrameGroupBy.mean()`.

    """
    if column is not None:
        grouped_mean = gb.mean(**kwargs)[column]
    else:
        grouped_mean = gb.mean(**kwargs)
    return grouped_mean


@Pipeable
@append_docstring(pd.core.groupby.generic.DataFrameGroupBy.sum)
def Sum(gb, column=None, **kwargs):
    """
    Implements `pandas.core.groupby.generic.DataFrameGroupBy.sum()`.

    :param *args:
        Any args accepted by `pandas.core.groupby.generic.DataFrameGroupBy.sum()`.
    :param **kwargs:
        Any kwargs accepted by `pandas.core.groupby.generic.DataFrameGroupBy.sum()`.

    """
    if column is not None:
        grouped_sum = gb.sum(**kwargs)[column]
    else:
        grouped_sum = gb.sum(**kwargs)
    return grouped_sum


