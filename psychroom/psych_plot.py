import numpy as np
from numpy import arctan, diff, mod, pi
import matplotlib.pyplot as plt

from CoolProp.HumidAirProp import HAProps as air


def plot():
    """Create a psychrometric chart using CoolProp and PyPlot"""
    N = 500
    C2K = 273.15
    P = 101.325
    tdb = np.linspace(start=-10., stop=40.0, num=N)
    D_scale = np.linspace(start=-10., stop=40.0, num=N)
    dew_point = np.array(
        [1000. * air('W', 'T', tdb[i] + C2K, 'D', D_scale[i] + C2K, 'P', P)
         for i in range(N)])
    rh_scale = np.linspace(start=0.1, stop=0.9, num=9)
    rh_lines = [[1000. * air('W', 'T', db+C2K, 'R', rh, 'P', P)
                 for db in tdb] for rh in rh_scale]
    h_scale = np.arange(-10., 110., 5.)
    h_lines = [[1000. * air('W', 'T', db+C2K, 'H', h, 'P', P)
                for db in tdb] for h in h_scale]
#    v_scale = np.arange(0.76, 0.92, 0.02)
#    v_lines = [[1000. * air('W', 'T', db+C2K, 'V', v, 'P', P)
#                for db in tdb] for v in v_scale]
#    wb_scale = np.arange(5., 25., 1.)
#    wb_lines = [[air('W', 'T', db+C2K, 'B', wb, 'P', P)
#                 if db > wb else np.nan for db in tdb] for wb in wb_scale]

    fig = plt.figure(figsize=(11., 8.5))
    ax = fig.add_subplot(111)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_xlim((-10., 40.))
    ax.set_xticks(np.arange(-10, 41, 5))
    ax.set_ylim((0., 25.))
    ax.set_yticks(np.arange(0., 25., 2.))
    ax.plot(tdb, dew_point, 'k-', lw=1)
    [ax.plot((x, x), (0, 1000. * air('W', 'T', x+C2K, 'R', 1., 'P', P)),
             c='k', lw=0.25, alpha=0.2) if mod(i, 5) else
     ax.plot((x, x), (0, 1000. * air('W', 'T', x+C2K, 'R', 1., 'P', P)),
             c='k', lw=1.0, alpha=0.5)
     for i, x in enumerate(np.arange(-10., 41., 1.))]
    [ax.plot((air('T', 'W', x/1000., 'R', 1., 'P', P) - C2K, 40.), (x, x),
             c='k', lw=0.25, alpha=0.2) if mod(i+1, 4) else
     ax.plot((air('T', 'W', x/1000., 'R', 1., 'P', P) - C2K, 40.), (x, x),
             c='k', lw=1.0, alpha=0.5)
     for i, x in enumerate(np.arange(0.5, 25., 0.5))]
    [ax.plot(tdb, rh_line, 'g-', lw=1, alpha=0.5) for rh_line in rh_lines]
    [ax.plot(tdb, h_line, 'b-', lw=0.5, alpha=0.5) for h_line in h_lines]
#    [ax.plot(tdb, v_line, 'r-', lw=0.5, alpha=0.5) for v_line in v_lines]
    ax.fill_between(tdb, 25. * np.ones(len(dew_point)),
                    dew_point + 0.05, color='w', zorder=1000)

    rh_args = {'fontsize': 8, 'ha': 'left', 'va': 'center', 'color': 'green',
               'bbox': {'fc': 'white', 'ec': 'white', 'alpha': 0.2}}
    [ax.text(tdb[210-4*i], w[210-3*i], "{0}%".format(10*(i+1)),
             rotation=arctan(diff(w[209:211])/diff(tdb[209:211]))[0]*180./pi,
             **rh_args) for i, w in enumerate(rh_lines)]
    h_args = {'fontsize': 8, 'ha': 'left', 'va': 'top', 'color': 'blue',
              'bbox': {'fc': 'white', 'ec': 'white', 'alpha': 0.2}}
    [ax.text(tdb[483], w[483], "{0}".format(int(h_scale[i+11])),
             rotation=arctan(diff(w[482:484])/diff(tdb[482:484]))[0]*180./pi,
             **h_args) for i, w in enumerate(h_lines[11:23])]
    [ax.text(air('T', 'H', h_scale[i+1], 'W', 0.75/1000., 'P', P) - 273.15,
             0.75, "{0}".format(int(h_scale[i+1])),
             rotation=arctan(diff(w[482:484])/diff(tdb[482:484]))[0]*180./pi,
             **h_args) if h_scale[i+1] > -5 else
     ax.text(air('T', 'H', h_scale[i+1], 'W', 1./1000., 'P', P) - 273.15,
             1., "{0} kJ/kg".format(int(h_scale[i+1])),
             rotation=arctan(diff(w[50:52])/diff(tdb[50:52]))[0]*180./pi,
             **h_args) for i, w in enumerate(h_lines[1:11])]

    ax.set_xlabel("Dry-Bulb Temperature [C]")
    ax.set_ylabel("Humidity Ratio [grams moisture per kilorgram dry air]")

    fig.savefig('./test.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.close('all')
