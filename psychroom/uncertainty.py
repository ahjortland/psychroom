"""Uncertainty of data input/output handler functions."""

import pandas as pd
import pdb
import numpy as np

from uncer_class import Info_uncer, eval_uncer
from frames import monkey_patch

monkey_patch()


def load_uncer(filepath, sep=';'):
    """Load the standard file with uncertainty information

    Parameters
    ----------
    filepath : str
        directory containing experimental data files

    Returns
    -------
    uncer : list
        list of Info_uncer

    """

    uncer = []

    # start reading files
    with open(filepath, 'r') as f:
        # only continue if the first line is "[uncertainty]"
        if read_entry(f, sep)[0] == '[uncertainty]':
            line = read_entry(f, sep)  # skip line
            line = read_entry(f, sep)
            while not line[0] == '':
                if len(line) == 1:  # assume zero uncertainty
                    info = Info_uncer(x_name=line[0], expr=0.)
                else:
                    info = Info_uncer(x_name=line[:-1], expr=line[-1])
                uncer.append(info)
                line = read_entry(f, sep)

    return uncer


def read_entry(handle, sep=';'):
    """
    Read entries in the row in the file that its format is defined by seperator
    sep

    Parmeters:
    ---------
    handle:     file handle
        test data file handle

    Results:
    ---------
    output:     list
        list of strings seperated by sep

    """

    return map(str.strip, handle.readline().strip(' \n'+sep).split(sep))


def uncer_cal(result, uncer):
    """
    Return another pandas.Dataframe with information of the uncertainty at each
    value obtained from the experiment

    Parmeters:
    ---------
    result  :   pandas Dataframe
        data from experiment from io_.read_()
    uncer   :   list of Info_uncer
        information related to the uncertainty calculation from load_uncer

    Results:
    ---------
    uncer_result   :    pandas Dataframe
        uncertainty of data from experiment

    """

    # default zero uncertainty
    uncer_result = pd.DataFrame(np.zeros((
        len(result.index), len(result.columns)
    )), index=result.index, columns=result.columns)

    # the uncertainty units and descriptions should be linked with each other
    uncer_result._units = result._units
    uncer_result._descriptions = result._descriptions

    # assign values
    for info in uncer:
        uncer_result[info.x_name[0]] = eval_uncer(info.x_name[0], result, info)

    return uncer_result

if __name__ == '__main__':

    import io_ as io2

    path = './test_data/data_uncer_003.htf'
    uncer_path = './test_data/uncertainty_003.htf'
    df = io2.read_(path, **{'parse_dates': True})
    uncer = load_uncer(uncer_path, ';')
    uncer_result = uncer_cal(df, uncer)
    print(uncer)
    print(uncer_result)
