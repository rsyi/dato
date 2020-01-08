"""
Matplotlib plotting functions.
"""

from ..base import Pipeable, use_first_arg_only
from .base import _ModelSpec

@Pipeable
def InitModel(df, label, *args, **kwargs):
    """Specify the dataframe and the label for a machine learning model, and set up the class object that will act as accumulator.
    """
    X_columns = [col for col in df.columns if col!=label]
    newdf = df[X_columns + [label]]
    m = _ModelSpec(newdf)
    return (m, newdf)


@use_first_arg_only
@Pipeable
def TrainTestSplit(m, **kwargs):
    X_train, X_test, y_train, y_test = m.train_test_split(m.X, m.y, **kwargs)
    return (m, X_train, X_test, y_train, y_test)


