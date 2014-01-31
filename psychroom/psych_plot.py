# -*- coding: utf-8 -*-
"""A set of tools for plotting psychrometric charts."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from CoolProp.HumidAirProp import HAProps as air

from unit import Unit


def psychrometric_chart(P_AMB=101.325,
                        units=None, lines={'H', 'R', 'V', 'T', 'W'}, **kwargs):
    """Make a psychrometric chart on a set of axes.

    Parameters
    ----------
    P_AMB : float
        ambient pressure used for air property evaluations
    lines = {'H', 'R', 'V', 'T', 'W'} | None
        plot constant property lines

    Returns
    -------
    ax_or_axes : matplotlib.AxesSubplot or list of them

    """

    # Define some useful conversion function, for convenience.
    convert = {
        'T': Unit('K').to('degC'),
        'W': Unit('kg').to('g'),
    }

    # Set the chart axes limits, dry-bulb [K] and
    # humidity ratio [kg/kg.da].
    T_LIMS = np.array((263.15, 333.15))
    W_LIMS = np.array((0., 0.033))
    # Make arrays of dry-bulb temperatures and humidity ratios for
    # property calculations.
    T = np.linspace(T_LIMS[0], T_LIMS[1], 100)
    W = np.linspace(W_LIMS[0], W_LIMS[1], 100)

    # Calculate the dew-point line using humid air property relations.
    D = np.array([air('W', 'T', t, 'R', 1, 'P', P_AMB) for t in T])

    # Generate lines of constant enthalpy, specific volume, wetbulb,
    # and relative humidity.
    prop_args = {
        'H': ('H', (-10, 145.), 5., T, P_AMB),
        'R': ('R', (0.1, 0.9), 0.1, T, P_AMB),
        'V': ('V', (0.75, 0.95), 0.05, T, P_AMB),
    }

    line_args = {
        'H': {'color': 'blue', 'linewidth': 0.3, 'alpha': 0.3},
        'R': {'color': 'green', 'linewidth': 0.3, 'alpha': 0.3},
        'V': {'color': 'magenta', 'linewidth': 0.3, 'alpha': 0.3},
        'D': {'color': 'black', 'linewidth': 1.5, 'alpha': 0.8},
        'T': {'color': 'black', 'linewidth': 0.3, 'alpha': 0.5},
        'W': {'color': 'black', 'linewidth': 0.3, 'alpha': 0.5},
    }

    # As a first implementation, create a new figure and axis.
    fig, ax = plt.subplots(1, 1)
    # Plot dew point line.
    ax.plot(convert['T'](T), convert['W'](D), **line_args['D'])

    # Determine which grid lines and constant property lines to plot.
    lines = lines if isinstance(lines, set) else set(*lines)
    grid = lines & {'T', 'W'}
    lines = lines - grid
    # Plot constant property lines.
    if lines:
        try:
            for prop in lines:
                for val, x in _make_property_lines(*prop_args[prop]).items():
                    ax.plot(convert['T'](T), convert['W'](x),
                            **line_args[prop])
                    # TODO Add line labels to these property lines.
        except KeyError as e:
            raise KeyError(
                "Unrecognized property {} from lines parameter".format(e)
            )
    # Make grid lines for the drybulb and humidity ratio axes.
    if 'T' in grid:
        ax.vlines(np.unique(np.round(convert['T'](T))),
                  *convert['W'](W_LIMS), **line_args['T'])
    if 'W' in grid:
        ax.hlines(np.unique(np.round(convert['W'](W))),
                  *convert['T'](T_LIMS), **line_args['W'])

    # This is a trick to make it appear the upper-left portion of the
    # chart is empty.
    ax.fill_between(convert['T'](T), convert['W'](D + 7E-5),
                    convert['W'](W_LIMS[1]), color='w', zorder=1000)

    # Format the chart axes in the common psychrometric chart style.
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position('right')
    # Set the axis limits to the drybulb and humidity ratio limits.
    ax.set_xlim(convert['T'](T_LIMS))
    ax.set_ylim(convert['W'](W_LIMS))
    # Set the main axes labels.
    ax.set_xlabel(r'Drybulb Temperature [{}]'.format(Unit('degC')))
    ax.set_ylabel(r'Humidity Ratio [{}]'.format('g/kg-d.a.'))
    ax.text(0.01, 0.98,
            r'$P_\mathrm{{amb}}$={0:6.3f} {1}'.format(P_AMB, Unit('kPa')),
            horizontalalignment='left', verticalalignment='top',
            transform=ax.transAxes, zorder=1001)

    return fig, ax


def map_(func, args, P_ATM=101.325, nbins=39, fig=None, ax=None, cmap=None,
         label=''):
    """Map a function over points and plot contours psychrometric chart.

    func : function
        function mapped about the psychrometric chart
    args : ('T' | 'W' | 'H' | etc. )
        air properties used as inputs to the mapped function.

    """

    if not fig:
        fig, ax = psychrometric_chart()
    fig.subplots_adjust(bottom=0.1, right=1.0)
    cmap = cmap or plt.get_cmap()
    plt.close('all')

    T_MIN, T_MAX = ax.get_xlim()
    W_MIN, W_MAX = ax.get_ylim()
    dT = (T_MAX - T_MIN) / 100.
    dW = (W_MAX - W_MIN) / 100.

    W, T = np.mgrid[slice(W_MIN, W_MAX + dW, dW), slice(T_MIN, T_MAX + dT, dT)]

    calculate_property = {
        'T': lambda t, w: t,
        'W': lambda t, w: w,
        'H': lambda t, w: air('H', 'T', t + 273.15, 'W', w / 1000., 'P', P_ATM)
    }

    Z = []
    for item in zip(T, W):
        for t, w in zip(*item):
            Z.append(func([calculate_property[prop](t, w) for prop in args]))
    Z = np.array(Z).reshape(T.shape)
    # T and W are bounds, so Z should be the value inside those bounds.
    # Therefore, remove the last value from the z array.
    Z = Z[:-1, :-1]
    # Make bins for defining the contour bounds.
    levels = MaxNLocator(nbins=nbins).tick_values(Z.min(), Z.max())

    # Contours are point based plots, so convert our bounds into point
    # centers
    p = ax.contourf(T[:-1, :-1] + dT / 2., W[:-1, :-1] + dW / 2., Z,
                    levels=levels, cmap=cmap, alpha=0.8, drawedges=False)
    cb = fig.colorbar(p, ax=ax, pad=0.1)
    cb.solids.set_edgecolor('face')
    cb.set_label(label)

    return fig, ax


def plot_process(T, W, X=None, labels=None, fig=None, ax=None, cmap=None):
    """Plot a process on a psychrometric chart."""

    if not fig:
        fig, ax = psychrometric_chart()
    fig.subplots_adjust(bottom=0.1, right=1.0)
    cmap = cmap or plt.get_cmap()
    plt.close('all')

    if not X:
        ax.scatter(T, W, 10, marker='o', color='black')
    else:
        ax.scatter(T, W, 10, X, marker='o', cmap=cmap)
    if labels:
        for t, w, l in zip(T, W, labels):
            ax.annotate(l, xy=(t, w), xytext=(5, -5),
                        textcoords='offset points', horizontalalignment='left',
                        verticalalignment='top', fontsize=9)


def _test_psych_chart(**kwargs):
    """Test function of psychrometric chart function."""

    h = air('H', 'T', 28. + 273.15, 'R', 0.4, 'P', 101.325)
    vent_load = lambda x: x[0] - h

    T = (28., 35., 31., 14.)
    W = (10., 20., 15, 8.)
    labels = ('RA', 'OA', 'MA', 'SA')

    fig, ax = psychrometric_chart(lines={'T', 'W', 'R'})
    map_(vent_load, ('H', ), nbins=12, fig=fig, ax=ax,
         cmap=plt.get_cmap('CMRmap'), label='Ventilation Load [kJ/kg]')
    plot_process(T, W, labels=labels, fig=fig, ax=ax)
    fig.savefig('./test.pdf', bbox_inches='tight')
    fig.savefig('./test.png', format='png', dpi=600, bbox_inches='tight')
    plt.close('all')

    return fig, ax


def _make_property_lines(prop, lims, step, T, P):
    """Calculate constant property lines for a given range of drybulb.

    Parameters
    ----------
    prop : str
        humid air property string
    lims : (float, float)
        limits of the property evaluations
    step : float
        increments between each property line within limits
    T : array like
        drybulb temperature values for property evaluations [K]
    P : float
        ambient pressure used for evaluation [kPa]

    Returns
    -------
    lines = {float: np.array}
        dictionary of constant property lines as arrays

    """
    lines = {
        x: np.array([air('W', 'T', t, prop, x, 'P', P) for t in T])
        for x in np.arange(lims[0], lims[1] + step, step)
    }

    return lines
