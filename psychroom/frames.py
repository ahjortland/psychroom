"""Monkey-patched pandas data frame object for storing attributes."""

import pandas as pd

from .tools import (_get_metadata, _update_metadata, units, descriptions,
                    explore, convert)

pd.set_option('chained_assignment', None)


def monkey_patch():
    """Monkey patch the pandas data frame object."""

    pd.DataFrame._get_metadata = _get_metadata
    pd.DataFrame._update_metadata = _update_metadata

    pd.DataFrame.units = units
    pd.DataFrame.descriptions = descriptions
    pd.DataFrame.explore = explore
    pd.DataFrame.convert = convert
