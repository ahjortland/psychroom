"""Uncertainty of data input/output handler functions."""

import pdb

import pandas as pd
import numpy as np
import sympy as sym
from sympy.core.sympify import SympifyError

from frames import monkey_patch

monkey_patch()


class info_uncer():
    """To store mathematical expressions to calculate the uncertainty of
       the variables

    Parameters
    ----------
    x_name  : list of string
        name of the variables of which the uncertainty is dependent on; note
        that the zeroth entry is also the variable of which the uncertainty is
        calculated
    expr    : sympy expressions
        mathematical expressions or values of uncertainties, in which
        variables are represented by x0, x1, x2, etc.

    """

    def __init__(self, x_name=['-'], expr=0.):
        self.x_name = x_name
        self.expr = expr

    def __setattr__(self, name, value):
        # store the string into absolute values or sympy expressions
        if name == "expr":
            try:
                expr = sym.sympify(value)
                self.__dict__[name] = expr
            except SympifyError:
                print('Cannot convert '+value+' into Sympy expressions')
                self.__dict__[name] = sym.sympify('nan')
        else:
            self.__dict__[name] = value
            if name == 'x_name':  # reset variables everytime x_name is changed
                self._set_var()

    def __repr__(self):
        # printing methods
        output = "UncertaintyInfo(Eqn='"+str(self.expr)+"', "
        output = output+"Variables=['"+self.x_name[0]+"'"
        if len(self.x_name) > 1:
            for i in range(1, len(self.x_name)):
                output = output+", '"+self.x_name[i]+"'"
                if i > 3:
                    output = output+',......'
                    break
        output = output+"])"
        return output

    def _set_var(self):
        # setting variables to evaluate sympy expressions
        if len(self.x_name) == 1:
            self.x_var = [sym.symbols('x0')]
        else:
            self.x_var = sym.symbols('x0:'+str(len(self.x_name)))


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
    info        :   Info_uncer
        information related to the uncertainty calculation from load_uncer

    Results:
    ---------
    uncer_cal   :   list
        uncertainty of data calculated from data and info

    """

    range_num = range(len(info.x_name))

    def _var_dict(index):
        var_dict = {}
        for i in range_num:
            var_dict[info.x_var[i]] = data[info.x_name[i]][index]
        return var_dict

    # convert all the final results to numpy float64
    if info.expr.is_number:
        uncer_cal = [np.float64(info.expr.evalf())]*len(data.index)
    else:
        uncer_cal = [
            np.float(info.expr.evalf(subs=_var_dict(index)))
            for index in data.index
        ]
    return uncer_cal
