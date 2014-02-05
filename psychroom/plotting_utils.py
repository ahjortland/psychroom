"""Utility functions used for plotting."""

import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import sqrt


def set_rcparams(context='notebook', style='nogrid', font_params={},
                 latex=None, dpi=None):
    """Use custom rcParams tailored to different contexts and styles.

    Parameters
    ----------
    context : notebook | talk | paper | article | report | poster | beamer
        contextual setting produced figures are targeting
    style : darkgrid | whitegrid | nogrid | ticks
        context style modifier that changes the look of axes
    font_params : {}
        dict containing fontfamily and font parameters
    latex : {}
        dict containing latex parameters

    """

    set_fonts(context.casefold(), **font_params)
    set_figure(context.casefold())
    set_axes(style.casefold())


def set_fonts(context, **kwargs):
    """Set font sizes of figure based on context.

    Parameters
    ----------
    context : notebook | talk | paper | article | report | poster | beamer
        contextual setting produced figures are targeting
    fontsize : int
        base font size (used for axis labels)
    fontfamily : serif | sans-serif | monospace
        font family used for text in figures
    serif : str
        serif font name (must be present in system)
    sans_serif : str
        sans-serif font name (must be present in system)
    monospace : str
        monospace font name (must be present in system)

    """

    base = kwargs['fontsize'] if 'fontsize' in kwargs else None
    fontfamily = kwargs['fontfamily'] if 'fontfamily' in kwargs else None
    serif = kwargs['serif'] if 'serif' in kwargs else None
    sans_serif = kwargs['sans-serif'] if 'sans-serif' in kwargs else None
    monospace = kwargs['monospace'] if 'monospace' in kwargs else None

    if context in ('paper', 'article', 'report'):
        base = base or 11
        params = {
            'axes.labelsize': base,
            'axes.titlesize': base + 1,
            'xtick.labelsize': base - 1,
            'ytick.labelsize': base - 1,
            'legend.fontsize': base - 1,
            'font.family': fontfamily or 'serif',
        }
    elif context in ('talk', 'beamer', 'presentation', ):
        base = base or 16
        params = {
            'axes.labelsize': base,
            'axes.titlesize': base + 3,
            'xtick.labelsize': base - 2,
            'ytick.labelsize': base - 2,
            'legend.fontsize': base - 3,
            'font.family': fontfamily or 'sans-serif',
        }
    elif context in ('notebook', ):
        base = base or 11
        params = {
            'axes.labelsize': base,
            'axes.titlesize': base + 1,
            'xtick.labelsize': base - 1,
            'ytick.labelsize': base - 1,
            'legend.fontsize': base - 1,
            'font.family': fontfamily or 'sans-serif',
        }
    elif context in ('poster', ):
        base = base or 18
        params = {
            'axes.labelsize': base,
            'axes.titlesize': base + 4,
            'xtick.labelsize': base - 2,
            'ytick.labelsize': base - 2,
            'legend.fontsize': base - 2,
            'font.family': fontfamily or 'sans-serif',
        }

    # TODO Move this to a latex parameter setting function.
    if context in ('article', 'report', 'beamer', ):
        params['text.usetex'] = True
        params['text.latex.unicode'] = True

    params['font.serif'] = serif or 'Computer Modern Roman'
    params['font.sans-serif'] = sans_serif or 'Computer Modern Sans serif'
    params['font.monospace'] = monospace or 'Computer Modern Typewriter'

    mpl.rcParams.update(params)


def set_axis_style(style, context, latex_params=None, font=None,
                   gridweight=None):
    """Set the axis style.

    Parameters
    ----------
    style : darkgrid | whitegrid | nogrid | ticks
        Style of the axis background.
    context : notebook | talk | paper | poster
        Intended context for resulting figures.
    latex_params : latex DocumentClass parameters
        DocumentClass parameters used in intended latex document
        preamble.
    font : matplotlib font spec
        Font to use for text in the figures.
    gridweight : extra heavy | heavy | medium | light | None

    """

    # Validate the arguments.
    if not {'darkgrid', 'whitegrid', 'nogrid', 'ticks'} & {style}:
        raise ValueError("Style '{}' not recognized.".format(style))

    if not {'notebook', 'talk', 'paper', 'poster'} & {context}:
        raise ValueError("Context '{}' not recognized.".format(context))

    # Determine the axis parameters.

    # Turn ticks off; they will get turned back on in 'ticks' style.
    _set_tick_size(0, 0)

    GRID_WEIGHTS = {
        'extra heavy': 1.5,
        'heavy': 1.1,
        'medium': 0.8,
        'light': 0.5,
    }
    if gridweight is None:
        if context == 'paper':
            glw = GRID_WEIGHTS['light']
        else:
            glw = GRID_WEIGHTS['medium']
    elif isinstance(gridweight, float) or isinstance(gridweight, int):
        glw = gridweight
    else:
        glw = GRID_WEIGHTS[gridweight]

    if style == 'darkgrid':
        ax_params = {
            'axes.facecolor': '#EAEAF2',
            'axes.edgecolor': 'white',
            'axes.linewidth': 0,
            'axes.grid': True,
            'axes.axisbelow': True,
            'grid.color': 'white',
            'grid.linestyle': '-',
            'grid.linewidth': glw
        }
    elif style == 'whitegrid':
        lw = 1.0 if context in ('paper', 'article') else 1.7
        ax_params = {
            'axes.facecolor': 'white',
            'axes.edgecolor': '#CCCCCC',
            'axes.linewidth': lw,
            'axes.grid': True,
            'axes.axisbelow': True,
            'grid.color': '#DDDDDD',
            'grid.linestyle': '-',
            'grid.linewidth': glw
        }
    elif style == 'nogrid':
        ax_params = {
            'axes.grid': False,
            'axes.facecolor': 'white',
            'axes.edgecolor': 'black',
            'axes.linewidth': 1
        }
    elif style == 'ticks':
        ticksize = 3. if context in ('paper', 'article') else 6.
        tickwidth = 0.5 if context in ('paper', 'article') else 1.
        ax_params = {
            'axes.grid': False,
            'axes.facecolor': 'white',
            'axes.edgecolor': 'black',
            'axes.linewidth': 1,
            'xtick.direction': 'out',
            'ytick.direction': 'out',
            'xtick.major.width': tickwidth,
            'ytick.major.width': tickwidth,
            'xtick.minor.width': tickwidth,
            'xtick.minor.width': tickwidth,
            'xtick.major.size': ticksize,
            'xtick.minor.size': ticksize / 2.,
            'ytick.major.size': ticksize,
            'ytick.minor.size': ticksize / 2.
        }

    mpl.rcParams.update(ax_params)


def _set_tick_size(major, minor):
    """Set the axis tick size parameters.

    Parameters
    ----------
    major : float
        major tick size parameter
    minor : float
        minor tick size parameter

    """
    mpl.rc("xtick.major", size=major)
    mpl.rc("xtick.minor", size=minor)
    mpl.rc("ytick.major", size=major)
    mpl.rc("ytick.minor", size=minor)


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

    if style in ('academic', 'publication', ):
        params = {
            # 'axes.color_cycle': default_colors,
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


def latex_figure_size(**kwargs):
    """Set parameters that make latex figures pretty."""

    PT_TO_IN = 1. / 72.27  # point to inches conversion
    GOLDEN_MEAN = 0.5 * (sqrt(5.) - 1.)  # aesthetic ratio

    column_widths = {
        1: {10: 345.0, 11: 360.0, 12: 390.0},
        2: {10: 167.5, 11: 175.0, 12: 190.0},
        3: {10: 108.3, 11: 113.3, 12: 123.3},
        4: {10: 78.75, 11: 82.5, 12: 90.0},
        5: {10: 61.0, 11: 64.0, 12: 70.0},
    }

    columns = kwargs['columns'] if 'columns' in kwargs else 1
    fontsize = kwargs['fontsize'] if 'fontsize' in kwargs else 11

    figure_width = column_widths[columns][fontsize] * PT_TO_IN
    figure_height = figure_width * GOLDEN_MEAN

    return figure_width, figure_height


def use_pgf(texsystem='xelatex', rcfonts=True, preamble=None):
    """Use the pgf backend to export figures directly as pgf drawings.

    Parameters
    ----------
    texsystem : xelatex | lualatex | pdflatex
    rcfonts : True | False
        Use the fonts defined in the rcparams
    preamble : [str]
        Lines to be included in the latex preamble.

    """

    preamble = preamble or [
        r'\usepackage{amsmath}',
        r'\usepackage{amssymb}',
        r'\usepackage{color}',
        r'\usepackage{siunitx}',
    ]

    mpl.use('pgf')
    pgf_with_preamble = {
        'pgf.rcfonts': rcfonts,
        'pfg.texsystem': texsystem,
        'pgf.preamble': preamble,
    }
    mpl.rcParams.update(pgf_with_preamble)


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
