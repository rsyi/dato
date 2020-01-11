"""
Static plotting functions (e.g. matplotlib, seaborn).

"""
import functools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from seaborn import FacetGrid

from ..base import Pipeable, unpack_input
from ..style import mpl_style_decorator

line_kwargs = {
    'marker': 'o',
    'markersize': 3,
    'linewidth': 1,
    'linestyle': '-',
}




@Pipeable
@mpl_style_decorator
def Plot(data, kind='line', x=None, y=None, row=None, col=None, **kwargs):

    function_map = {
        'scatter': plt.scatter,
        'line': plt.plot,
        'hist': plt.hist,
        'bar': plt.bar,
        'barh': plt.barh,
        'box': plt.boxplot,
        'hexbin': plt.hexbin,
    }


    # Preprocess the `data` input.
    if type(data) == tuple:
        x = data[0]
        y = data[1]
    else:
        if x is not None:
            x = data[x]
        else:
            x = data
        if y is not None:
            y = data[y]

    # Set default kwargs.
    if kind=='scatter':
        if 'alpha' not in kwargs:
            kwargs['alpha'] = 0.5

    # Plot.
    if (row is not None) or (col is not None):
        g = FacetGrid(data=data, row=row, col=col, **kwargs)
        g = g.map(function_map[kind], x, y, **kwargs)
    else:
        if kind=='hist':
            g = function_map[kind](x, **kwargs)
        elif kind=='line':
            if y is not None:
                g = function_map[kind](x, y, **kwargs)
            else:
                g = function_map[kind](x, **kwargs)
        elif kind=='bar':
            g = function_map[kind](x=x, height=y, **kwargs)
        elif kind=='barh':
            g = function_map[kind](x=x, width=y, **kwargs)
        else:
            g = function_map[kind](x, y, **kwargs)

    # Deal with datetimes.
    fig = plt.gcf()
    fig.autofmt_xdate()

    return g


@unpack_input
@Pipeable
@mpl_style_decorator
def Scatter(*args, **kwargs):

    if 'alpha' not in kwargs:
        kwargs['alpha'] = 0.5

    return plt.scatter(*args, **kwargs)


@Pipeable
@mpl_style_decorator
def LogLogHist(a, bins=10, range=None, normed=None, weights=None, density=None, **kwargs):
    """A log-log histogram.
    """

    # If there are no plot kwargs, use default style.
    if not kwargs:
        kwargs.update(line_kwargs)

    y, x = np.histogram(a, bins=bins, range=range, normed=normed, weights=weights, density=density)
    handle = plt.plot((x[1:] + x[:-1])/2, y, **kwargs)
    plt.xscale('log')
    plt.yscale('log')

    return handle


@Pipeable
@mpl_style_decorator
def Hist(*args, **kwargs):
    handle = plt.hist(*args, **kwargs)
    return handle



