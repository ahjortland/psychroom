# -*- coding: utf-8 -*-
"""Useful tools when dealing with Test Data Frames."""

from unit import ureg
from compat import PY3

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

    if PY3:
        explore_string = "Column: {0}\n\tDescription:\t{1}\n\tUnit:\t\t{2:P}"
    else:
        explore_string = "Column: {0}\n\tDescription:\t{1}\n\tUnit:\t\t{2}"

    if not keys:
        for desc, unit in zip(self.descriptions().items(),
                              self.units().items()):
            print(explore_string.format(desc[0], desc[1], unit[1]))
    else:
        pass


def convert(self, key, unit, overwrite=False):
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

    Returns
    -------
    result : data frame
        updated subset or entire data frame

    """

    dimensions = {
        '[temperature]': ureg['kelvin'].dimensionality,
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

    if not overwrite:
        result = self[key]
        for k, u in zip(key, old_unit):
            result[k] = self[k].apply(lambda x: conversion(x, u))
            result._units[k] = unit
        return result
    else:
        for k, u in zip(key, old_unit):
            self[k] = self[k].apply(lambda x: conversion(x, u))
            self._units[k] = unit
        return self[key]
