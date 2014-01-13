"""Useful tools when dealing with Test Data Frames."""

from unit import Unit


def get_units(self):
    """Return a dictionary of the units of each column in a data frame.

    Parameters
    ----------
    frame : pandas DataFrame
        test data frame

    Returns
    -------
    units : {}
        dictionary of column names (keys) with the units (values).

    """
    return {key: _unit(self[key]) for key in self.keys()}


def _unit(series):
    """Return the unit of a series if defined, else return undefined.

    Parameters
    ----------
    series : pandas Series

    Returns
    -------
    unit : unit.Unit
        the unit type of the series or an undefined Unit if it is
        undefined.

    """
    try:
        return series.unit
    except AttributeError:
        return Unit('undefined')


def update_units(frame):
    """Update the units attribute of a test data frame.

    Parameters
    ----------
    frame : pandas DataFrame
        experimental test data frame

    Returns
    -------
    result : pandas DataFrame
        copy of the original experimental test data frame with an
        updated (or added) units attribute.

    """

    result = frame.copy(deep=True)
    result.units = get_units(frame)
    for key, val in result.units.items():
        result[key].unit = val

    return result
