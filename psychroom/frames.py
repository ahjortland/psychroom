"""Monkey-patched pandas data frame object for storing attributes."""

import pandas as pd

import tools

pd.set_option('chained_assignment', None)


def monkey_patch():
    """Monkey patch the pandas data frame object."""

    pd.DataFrame._get_metadata = tools._get_metadata
    pd.DataFrame._update_metadata = tools._update_metadata

    pd.DataFrame.units = tools.units
    pd.DataFrame.descriptions = tools.descriptions
    pd.DataFrame.explore = tools.explore
    pd.DataFrame.convert = tools.convert
