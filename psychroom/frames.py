"""Monkey-patched pandas data frame object for storing attributes."""

import pandas as pd

import tools


def monkey_patch():
    """Monkey patch the pandas data frame object."""

    pd.DataFrame.get_units = tools.get_units
