# -*- coding: utf-8 -*-
"""Methods for evaluating measurement uncertainty."""

import numpy as np
from sympy import symbols, sympify, SympifyError

from .unit import ureg


class UncertaintyInfo(object):

    """Object used to evaluate measurement uncertainty.

    Parameters
    ----------
    names : [strings]
        List of the names of the dependent variables used in the
        uncertainty calculation. Note, the zeroth element is always the
        variable which the uncertainty is evaluated, by convention.
    units : [pint Quantity]
        List of the units corresponding to each variable used in the
        uncertainty calculation.
    expr : sympy expression
        Mathematical expression (or constant) that quantifies the
        measurement uncertainty in terms of the arguments.

    """

    def __init__(self, names=[''], units=None, expr=None):
        self._xargs = symbols('x0:{}'.format(len(names)))
        self._names = {self.xargs[0]: names[0]}
        self._units = {}
        for xarg, name in zip(self.xargs[1:], names[1:]):
            self._names[xarg] = name
            self._units[xarg] = units[name] if units else ureg['']
        try:
            self._expr = sympify(expr) or sympify('nan')
        except SympifyError as e:
            raise e

    @property
    def names(self):
        return self._names

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, vals):
        self._units = {xarg: vals[name] for xarg, name in self.names.items()}

    @property
    def xargs(self):
        return self._xargs

    @property
    def expr(self):
        return self._expr

    def evaluate(self, frame):
        """Evaluate the measurement uncertainty expression.

        Parameters
        ----------
        frame : pandas DataFrame
            Experimental test data frame containing measurements.

        Returns
        -------
        result: pandas DataFrame or Series
            Measurement uncertainty calculated for each measurement
            using the uncertainty expression.

        """

        key = self.names[self.xargs[0]]
        result = frame.copy()
        result[key] = eval_uncertainty(key, result, self)

        return result[key]

    def __str__(self):
        output_string = (
            "Uncertainty information:\n" +
            "Name:\t{0} [{1:P}]\n".format(self.names[self.xargs[0]],
                                          self.units[self.xargs[0]].units) +
            "Args:\n"
        )
        for x, n, u in zip(self.xargs,
                           self.names.values(),
                           self.units.values()):
            output_string += " {0}:\t{1} [{2:P}]\n".format(x, n, u.units)
        output_string += "Expr:\t{}".format(self.expr)

        return output_string


def eval_uncertainty(key, data, info):
    """Evaluate the measurement uncertainty of a measurement.

    Parameters
    ----------
    key : string
        Name of the measurement.
    data : pandas DataFrame
        Experimental test data frame containing measurements.
    info : UncertaintyInfo
        Uncertainty information, in particular the required arguments
        and the mathematical expression.

    Returns
    -------
    result : pandas DataFrame
        Calculated measurement uncertainty for key.

    """

    items = info.names.items()
    f = lambda row: info.expr.evalf(subs={x: row[name] for x, name in items})

    result = np.array([f(row) for ind, row in data.iterrows()])

    return result


def parse_uncertainty_info(line):
    """Parse uncertainty information from standard test output file.

    Notes
    -----
    For information about the standard format for recording uncertainty
    information, see [Uncertainty Documentation]
    (https://github.com/ahjortland/psychroom/tree/master/docs)

    Parameters
    ----------
    line : string
        Line from standard output test file containing uncertainty
        information in the standard format.

    Returns
    -------
    result : UncertaintyInfo
        Object containing information about the mathematical expression
        used to calculate the measurement uncertainty as well as the
        variables used and their units.

    """

    # The component before the equal sign by convention corresponds to
    # variable whose uncertainty is defined by the expression.
    x0, info = [item.strip() for item in line.split('=')]

    # The remaining dependent variables of the mathematical
    # expression are defined within curly braces followed by the
    # actual mathematical expression that defines the measurement
    # uncertainty.
    xs, _, expr = [item.strip('{} ') for item in info.partition('}')]

    # In some cases, there may not be additional dependent variables.
    # In such a case, the partition function returns the mathematical
    # expression, followed by two empty strings. Switch these when this
    # happens.
    if not expr:
        xs, expr = expr, xs

    # Form a list of the arguments used to evaluate the mathematical
    # expression for uncertainty, filtering out empty strings.
    xs = [x0] + xs if isinstance(xs, list) else [x0] + [xs]
    xs = list(filter(None, xs))

    # Make sure the first element is the first component of the
    # original string.
    assert xs[0] == x0

    # Form an uncertainty information object that will be used
    # to evaluate the measurement uncertainty when required.
    result = UncertaintyInfo(names=xs, expr=expr)

    return xs[0], result
