"""Utility functions used for plotting."""

import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import sqrt


def set_rcparams(context='notebook', fontfamily=None, font=None,
                 style='academic', latex=False, dpi=None):
    """Set new matplotlib RC params."""

    # Set constant defaults.
    mpl.rc("lines", markeredgewidth=0, solid_capstyle="round")
    mpl.rc("image", cmap="CMRmap")

    set_fonts(context.casefold())
    set_figure(context.casefold())
    set_axes(style.casefold())


def set_fonts(context, base=None):
    """Set font sizes of figure based on context.

    Parameters
    ----------
    context : str
        document context (e.g. article, talk, poster,...)
    base : int, default None
        base font size (axis label size).  Other fonts will be sized in
        relation to this.

    """

    if context in ('paper', 'article', 'report'):
        base = base or 11
        params = {'axes.labelsize': base,
                  'axes.titlesize': base + 1,
                  'xtick.labelsize': base - 1,
                  'ytick.labelsize': base - 1,
                  'legend.fontsize': base - 1,
                  'font.family': 'serif', }
    elif context in ('talk', 'beamer', 'presentation', ):
        base = base or 16
        params = {'axes.labelsize': base,
                  'axes.titlesize': base + 3,
                  'xtick.labelsize': base - 2,
                  'ytick.labelsize': base - 2,
                  'legend.fontsize': base - 3,
                  'font.family': 'sans-serif', }
    elif context in ('notebook', ):
        base = base or 11
        params = {'axes.labelsize': base,
                  'axes.titlesize': base + 1,
                  'xtick.labelsize': base - 1,
                  'ytick.labelsize': base - 1,
                  'legend.fontsize': base - 1,
                  'font.family': 'sans-serif', }
    elif context in ('poster', ):
        base = base or 18
        params = {'axes.labelsize': base,
                  'axes.titlesize': base + 4,
                  'xtick.labelsize': base - 2,
                  'ytick.labelsize': base - 2,
                  'legend.fontsize': base - 2,
                  'font.family': 'sans-serif', }

    if context in ('article', 'report', 'beamer', ):
        params['text.usetex'] = True

    params['font.serif'] = 'Computer Modern Roman'
    params['font.sans-serif'] = 'Computer Modern Sans serif'
    params['font.monospace'] = 'Computer Modern Typewriter'

    mpl.rcParams.update(params)


def set_figure(context, size=None):
    """Set figure parameters according to context.

    Parameters
    ----------
    context : str
        document context (e.g. article, talk, poster,...)
    size : list, optional
        figure size dimensions in inches

    """

    params = {'figure.figsize': size or [5., 3.],
              'figure.dpi': 600,
              'savefig.bbox': 'tight',
              'savefig.dpi': 600,
              'savefig.extension': 'pdf',
              'savefig.format': 'pdf', }

    mpl.rcParams.update(params)


def set_axes(style='academic'):
    """Set axes parameters according to style.

    Parameters
    ----------
    style : str
        plot style string (e.g. academic,...)

    """

    default_colors = ['#377EB8', '#4DAF4A', '#E41A1C', '#984EA3', '#FF7F00',
                      '#FFFF33', '#A65628', '#F&81BF', '#999999']

    if style in ('academic', 'publication', ):
        params = {
            'axes.color_cycle': default_colors,
            'axes.edgecolor': 'k',
            'axes.facecolor': 'w',
            'axes.grid': False,
            'axes.linewidth': 1.0,
            'axes.unicode_minus': True,
            'axes.xmargin': 0.0,
            'axes.ymargin': 0.0,
            'grid.alpha': 1.0,
            'grid.color': 'k',
            'grid.linestyle': ':',
            'grid.linewidth': 0.5,
            'legend.borderaxespad': 0.5,
            'legend.borderpad': 0.4,
            'legend.columnspacing': 2.0,
            'legend.fancybox': True,
            'legend.frameon': True,
            'legend.handleheight': 0.7,
            'legend.handlelength': 1.5,
            'legend.handletextpad': 0.8,
            'legend.isaxes': True,
            'legend.labelspacing': 0.5,
            'legend.loc': 'upper right',
            'legend.markerscale': 1.0,
            'legend.numpoints': 2,
            'legend.scatterpoints': 1,
            'legend.shadow': False,
            'xtick.color': 'k',
            'xtick.direction': 'in',
            'xtick.major.pad': 2,
            'xtick.major.size': 4,
            'xtick.major.width': 0.5,
            'xtick.minor.pad': 2,
            'xtick.minor.size': 2,
            'xtick.minor.width': 0.5,
            'ytick.color': 'k',
            'ytick.direction': 'in',
            'ytick.major.pad': 2,
            'ytick.major.size': 4,
            'ytick.major.width': 0.5,
            'ytick.minor.pad': 2,
            'ytick.minor.size': 2,
            'ytick.minor.width': 0.5
        }

    mpl.rcParams.update(params)


def latex_figure_size(options):
    """Set parameters that make latex figures pretty."""

    PT_TO_IN = 1. / 72.27  # point to inches conversion
    GOLDEN_MEAN = 0.5 * (sqrt(5.) - 1.)  # aesthetic ratio

    column_widths = {
        1: {'10pt': 345.0, '11pt': 360.0, '12pt': 390.0},
        2: {'10pt': 167.5, '11pt': 175.0, '12pt': 190.0},
        3: {'10pt': 108.3, '11pt': 113.3, '12pt': 123.3},
        4: {'10pt': 78.75, '11pt': 82.5, '12pt': 90.0},
        5: {'10pt': 61.0, '11pt': 64.0, '12pt': 70.0},
    }

    columns = options['columns'] if 'columns' in options else 1
    fontsize = options['fontsize'] if 'fontsize' in options else '11pt'

    figure_width = column_widths[columns][fontsize] * PT_TO_IN
    figure_height = figure_width * GOLDEN_MEAN

    return [figure_width, figure_height]


def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """Minimize chartjunk.

    Minimize chartjunk by stripping out unnecesasry plot borders and
    axis ticks.

    The top/right/left/bottom keywords toggle whether the corresponding
    plot border is drawn.

    """

    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()
