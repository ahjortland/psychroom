"""Monkey-patched pandas data frame object for storing attributes."""

import pandas as pd

from .tools import (_get_metadata, _update_metadata, units, descriptions,
                    explore, convert)

pd.set_option('chained_assignment', None)


def monkey_patch():
    """Monkey patch the pandas data frame object."""

    pd.DataFrame._get_metadata = _get_metadata
    pd.DataFrame._update_metadata = _update_metadata

    pd.DataFrame.units = monkey_units
    pd.DataFrame.descriptions = monkey_descriptions
    pd.DataFrame.explore = monkey_explore
    pd.DataFrame.convert = monkey_convert


def monkey_convert(self, keys, new):
    return convert(self, keys, new)


def monkey_descriptions(self, keys=None):
    return descriptions(self, keys=keys)


def monkey_explore(self, keys=None):
    return explore(self, keys=keys)


def monkey_units(self, keys=None):
    return units(self, keys=keys)
