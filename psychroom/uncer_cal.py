"""Uncertainty evaluation functions."""

import pdb

import pandas as pd
import numpy as np
import sympy as sym
from pint import UnitRegistry

from .frames import monkey_patch
from .tools import convert

monkey_patch()
ureg = UnitRegistry()


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
    uncer_cal   :   pandas Series
        uncertainty of data calculated from data and info according to the unit
        of col_name in data

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
            if data._units[info.var[i]] == info.ori_unit[i]:
                var_dict[x_var[i]] = data[info.var[i]][index]
            else:
                var_dict[x_var[i]] = convert(
                    data, info.var[i], info.ori_unit[i], overwrite=False
                )[info.var[i]][index]
        return var_dict

    # unit conversion
    conver_fac = 1.
    if data._units[info.var[0]] != info.ori_unit[0]:
        if data._units[info.var[0]].dimensionality.__str__() != \
                '[temperature]':
            conver_fac = info.ori_unit[0].to(
                data._units[info.var[0]]
            ).magnitude
        else:
            old_unit = 'delta_'+info.ori_unit[0].units.__str__()
            new_unit = 'delta_'+data._units[info.var[0]].units.__str__()
            conver_fac = ureg[old_unit].to(ureg[new_unit]).magnitude

    # convert all the final results to numpy float64
    if info.eqn.is_number:
        uncer_cal = pd.Series(data=[
            np.float64(info.eqn.evalf())*conver_fac
        ]*len(data.index), index=data.index, name=info.var[0])
    else:
        uncer_cal = pd.Series(data=[
            np.float64(info.eqn.evalf(subs=_var_dict(index)))*conver_fac
            for index in data.index
        ], index=data.index, name=info.var[0])
    return uncer_cal
