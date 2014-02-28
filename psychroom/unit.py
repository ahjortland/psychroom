"""Unit base class, subclasses and associated methods."""

from pint import UnitRegistry

ureg = UnitRegistry()


def parse_unit_string(s):
    """Return a unit type from a string representation of a unit.

    This is simply a wrapper for the _Pint_ UnitRegistry.

    Parameters
    ----------
    s : string
        string representation of a unit, i.e. degC, watt, Btu/hr

    Returns
    -------
    q : pint.unit.Quantity
        a representation of a physical quantity from the _Pint_ pacakge
        used to handle units and make function unit-aware

    """
    return ureg[s]
