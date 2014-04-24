# -*- coding: utf-8 -*-
"""Useful tools when dealing with Test Data Frames."""

from copy import deepcopy
import pdb

from .unit import ureg
from .compat import PY3


def _get_metadata(self, attr, **kwargs):
    """Get a metadata property from a data frame.

    Parameters
    ----------
    attr : string
        metadata attribute name string

    Returns
    -------
    meta : {}
        metadata attribute dictionary

    """

    self._update_metadata(attr, **kwargs)
    try:
        return getattr(self, attr)
    except AttributeError as e:
        raise AttributeError(e)


def _update_metadata(self, attr, method=None):
    """Update a metadata property in a data frame.

    Parameters
    ----------
    attr : string
        metadata attribute name string

    """

    method = method or (lambda x: x)

    # Determine if there have been changes made to the units of each
    # column. First check if any columns have been dropped.
    meta = getattr(self, attr)
    old_keys = set(meta.keys())
    current_keys = set(self.keys())
    for key in old_keys - current_keys:
        meta.pop(key)

    # Now, check if any columns have been added.
    old_keys = set(meta.keys())
    for key in current_keys - old_keys:
        try:
            meta[key] = method(getattr(self[key], attr))
        except AttributeError:
            meta[key] = method(None)

    # Set updated metadata property.
    setattr(self, attr, meta)


def units(self, keys=None):
    """Return a dictionary of the units of each column in a data frame.

    Parameters
    ----------
    key : column name string
        When passed, the unit of the column named key is returned.

    Returns
    -------
    units : {} or Unit
        dictionary of column names (keys) with the units (values).

    """

    units = self._get_metadata('_units')
    if keys:
        units = {key: val for key, val in units.items() if key in keys}
        if len(units) == 1:
            return units.popitem()[1]
    else:
        return units


def descriptions(self, keys=None):
    """Return a dictionary of a description of each column in dataframe.

    Parameters
    ----------
    keys : column name string
        When passed, the unit of the column named key is returned.

    Returns
    -------
    description : {}
        dictionary of column names (keys) with descriptions (values).

    """

    desc = self._get_metadata('_descriptions')
    if keys:
        return {key: val for key, val in desc.items() if key in keys}
    else:
        return desc


def explore(self, keys=None):
    """Print a information describing each column of a data frame.

    Parameters
    ----------
    keys : column name string
        When passed, the unit of the column named key is returned.

    """

    explore_string = "Column: {0}\n\tDescription:\t{1}\n\tUnit:\t\t{2}"

    if 'uncertainty' in self.metadata:
        uncer_string = "\tUncer. Eqn.:\t{0}\n\tUncer. Var.:\t{1}"
        uncer_info = self.metadata['uncertainty']

    if not keys:
        for desc, unit in zip(self.descriptions().items(),
                              self.units().items()):
            print(explore_string.format(desc[0], desc[1], unit[1]))

            if 'uncertainty' in self.metadata:  # printing uncertainty
                var_string = uncer_info[desc[0]].var[0]
                # separate the variable names by comma
                for name in uncer_info[desc[0]].var[1:]:
                    var_string = var_string+', '+name
                if uncer_info[desc[0]].eqn.is_number:  # remove trailing zeros
                    eqn_string = repr(uncer_info[desc[0]].eqn).rstrip('0')
                else:
                    eqn_string = uncer_info[desc[0]].eqn
                print(uncer_string.format(
                    eqn_string, var_string
                ))
    else:
        pass


def convert(self, key, unit, overwrite=False, cal_uncer=True):
    """Convert a column in a data frame to a new unit.

    Parameters
    ----------
    key : column name string or dimension string
        column names which will be converted to new unit or a dimensionality
        identifier corresponding to the group of columns to be converted.
    unit : string or pint Unit
        unit identifying string or pint unit object
    overwrite : [False] | True
        original data frame values will be overwritten if True
    cal_uncer : False | [True]
        uncertainty will be recalculated and appended to the returned
        data frame if True.

    Returns
    -------
    result : data frame
        updated subset or entire data frame

    """

    dimensions = {
        '[temperature]': ureg['kelvin'].dimensionality,
        '[delta_temperature]': ureg['delta_kelvin'].dimensionality,
        '[pressure]': ureg['pascal'].dimensionality,
        '[power]': ureg['watt'].dimensionality,
        '[volume flow rate]': ureg['cubic meter per second'].dimensionality,
        '[mass flow rate]': ureg['kg per second'].dimensionality,
        '[enthalpy]': ureg['kilojoules per kilogram'].dimensionality,
        '[entropy]': ureg['kilojoules / kilogram / kelvin'].dimensionality,
        '[volume]': ureg['cubic meter'].dimensionality,
        '[mass]': ureg['kilogram'].dimensionality,
    }

    try:
        if key in dimensions:
            dim = dimensions[key]
            key = [
                k for k in self.keys() if self.units(k).dimensionality == dim
            ]
            old_unit = [self.units(k) for k in key]
        else:
            key = [key] if isinstance(key, str) else key
            old_unit = [self.units(key[0])]
    except TypeError:
        old_unit = [self.units(k) for k in key]

    if isinstance(unit, str):
        unit = ureg[unit]

    conversion = lambda x, u: (x * u).to(unit).magnitude

    def _uncer_conversion(key):
        if self.uncertainty._units[key].dimensionality.__str__() != \
                '[delta_temperature]':
            temp = convert(
                self.uncertainty, key, unit, overwrite=False,
                cal_uncer=False
            )
        else:
            temp = convert(
                self.uncertainty, key, 'delta_'+unit._units.__str__(),
                overwrite=False, cal_uncer=False
            )
        return temp[key], temp._units[key]

    if not overwrite:
        result = deepcopy(self[key])  # create new pandas Dataframe to return
        result._units = {}
        if cal_uncer:
            result.__dict__['uncertainty'] = deepcopy(self.uncertainty[key])
            result.__dict__['uncertainty']._units = {}
        for k, uu in zip(key, old_unit):
            result[k] = self[k].apply(lambda x: conversion(x, uu))
            result._units[k] = unit
            if cal_uncer:
                uncer, uncer_units = _uncer_conversion(k)
                result.__dict__['uncertainty'][k] = uncer
                result.__dict__['uncertainty']._units[k] = uncer_units
        return result
    else:
        for k, u in zip(key, old_unit):
            self[k] = self[k].apply(lambda x: conversion(x, u))
            self._units[k] = unit
            if cal_uncer:
                uncer, uncer_units = _uncer_conversion(k)
                self.__dict__['uncertainty'][k] = uncer
                self.__dict__['uncertainty']._units[k] = uncer_units
        return self[key]
