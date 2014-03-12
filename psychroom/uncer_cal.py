"""Uncertainty evaluation functions."""

import pdb

import pandas as pd
import numpy as np
import sympy as sym

from .frames import monkey_patch
from .tools import convert

monkey_patch()


def eval_uncer(col_name, data, info):
    """
    Returns a list containing the uncertainty of the variables in the
    column col_name in pandas Dataframe data

    Parmeters:
    ---------
    col_name    :   string
        name of the variable which uncertainty is evaluated
    data        :   pandas Dataframe
        data from experiment from io_.read_()
    info        :   nametuple(var, eqn, ori_unit)
        var: list of strings of names of variables
        eqn: sympy expressions for solution
        ori_unit: original unit of the variable in the equation

    Results:
    ---------
    uncer_cal   :   list
        uncertainty of data calculated from data and info

    """
    
    num = len(info.var)
    range_num = range(num)

    # setting variables to evaluate sympy expressions
    if num == 1:
        x_var = [sym.symbols('x0')]
    else:
        x_var = sym.symbols('x0:'+str(num))

    def _var_dict(index):
        var_dict = {}
        for i in range_num:
            if data[info.var[i]]._units == info.ori_unit[i]:
                var_dict[x_var[i]] = data[info.var[i]][index]
            else:
                var_dict[x_var[i]] = convert(
                    data, info.var[i], info.ori_unit[i], overwrite=False
                )[info.var[i]][index]
        return var_dict

    # convert all the final results to numpy float64
    if info.eqn.is_number:
        uncer_cal = [np.float64(info.eqn.evalf())]*len(data.index)
    else:
        uncer_cal = [
            np.float64(info.eqn.evalf(subs=_var_dict(index)))
            for index in data.index
        ]
    return uncer_cal
