"""Make a parity plot to compare data."""

# import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np

from plotting_utils import remove_border


def parity_plot(x, y, c=None, s=50, xerr=None, yerr=None,
                xlabel='', ylabel='', title=''):
    """Make a parity plot to compare data.

    Returns
    -------
    fig, ax : tuple

      - *fig* is the :class:`matplotlib.figure.Figure` object

      - *ax* can be either a single axis object or an array of axis
        objects if more than one subplot was created.  The dimensions of
        the resulting array can be controlled with the squeeze keyword

    """

    fig, ax = plt.subplots(1, 1)

    if c is not None:
        p = ax.scatter(x, y, s, c, zorder=4)
        cb = fig.colorbar(p)
        cb.solids.set_edgecolor('face')
    else:
        p = ax.scatter(x, y, s, c='b', zorder=4)
    if xerr is not None or yerr is not None:
        ax.errorbar(x, y, yerr, xerr, fmt=None, ecolor='black', errorevery=1)

    ax.axis('scaled')

    add_parity_lines(ax, x, y)

    ax.legend(loc='lower right')
    ax.grid()

    annotate_plot(ax, xlabel, ylabel, title)

    fig.show()

    return fig, ax


def add_parity_lines(ax, x, y):
    """Add maximum error bounds to the plot."""

    # Determine set of limits that will enclose all the data.
    lims = (
        np.min((ax.get_xlim(), ax.get_ylim())),
        np.max((ax.get_xlim(), ax.get_ylim()))
    )

    # Calculate residual statistics.
    residuals = x - y
    mad = np.max(np.abs(residuals))  # maximum absolute deviation
    std = np.std(residuals)  # standard deviation
    mu = np.mean(residuals)  # mean

    # Plot the line y = x, denoting a perfect comparison or fit.
    ax.plot(lims, lims, linestyle='-', linewidth=2, color='black')
    # Plot lines y = x +/- mad, denoting the maximum error bound.
    ax.plot(lims, lims + mad, 'r:', label='+/-{0:0.3f}'.format(mad))
    ax.plot(lims, lims - mad, 'r:')

    ax.plot(lims, lims + mu, linestyle=':', linewidth=1, color='black')

    # Plot shaded regions identifying the 1st, 2nd, and 3rd standard
    # deviation distances from the mean of the residuals.
    for val in range(1, 4):
        ax.fill_between(lims, lims + mu - val * std, lims + mu + val * std,
                        alpha=0.1, color='k')

    axi = inset_axes(ax, width='25%', height='25%', loc=2)
    _, bins, _ = axi.hist(residuals, normed=True, facecolor='black', alpha=0.5)
    x = np.linspace(mu - 3. * std, mu + 3. * std, 100)
    axi.plot(x, mlab.normpdf(x, mu, std),
             linestyle='-', linewidth=2, color='black')
    axi.set_yticklabels([])
    remove_border(axes=axi, left=False)


def annotate_plot(ax, xlabel, ylabel, title=None):
    """Add annotations to plot axis."""

    ax.set_xlabel(xlabel, fontsize=10, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=10, fontweight='bold')
    if title:
        ax.set_title(title, fontsize=10, fontweight='bold')
