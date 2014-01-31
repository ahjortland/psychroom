"""Unit of measurements library."""
from collections import namedtuple

from util import DEG_SYMBOL


def unit_library():
    """Unit library dictionary containing unit properties.

    Returns
    -------
    library : dict
        dictionary of unit type keys and property values

    """

    BASE_TO_BASE = lambda x: x
    props = namedtuple('UnitProperty', ['symbol', 'quantity', 'name',
                                        'base', 'to_base', 'from_base'])
    temperature = {
        'kelvin': props(
            quantity='temperature',
            name='Kelvin',
            symbol='K',
            base='kelvin',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'degrees celsius': props(
            quantity='temperature',
            name='degrees Celsius',
            symbol=DEG_SYMBOL + 'C',
            base='kelvin',
            to_base=lambda x: x + 273.15,
            from_base=lambda x: x - 273.15
        ),
        'degrees rankine': props(
            quantity='temperature',
            name='degrees Rankine',
            symbol=DEG_SYMBOL + 'R',
            base='kelvin',
            to_base=lambda x: (x - 491.67) / 1.8 + 273.15,
            from_base=lambda x: 1.8 * (x - 273.15) + 491.67
        ),
        'degrees fahrenheit': props(
            quantity='temperature',
            name='degrees Fahrenheit',
            symbol=DEG_SYMBOL + 'F',
            base='kelvin',
            to_base=lambda x: (x + 459.67) / 1.8,
            from_base=lambda x: 1.8 * x - 459.67
        ),
    }

    pressure = {
        'pascal': props(
            quantity='pressure',
            name='pascals',
            symbol='Pa',
            base='pascal',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'bar': props(
            quantity='pressure',
            name='bar',
            symbol='bar',
            base='pascal',
            to_base=lambda x: x * 10 ** 5,
            from_base=lambda x: x * 10 ** -5
        ),
        'standard atmosphere': props(
            quantity='pressure',
            name='standard atmosphere',
            symbol='atm',
            base='pascal',
            to_base=lambda x: 1.01325 * x * 10 ** 5,
            from_base=lambda x: 0.98692 * x * 10 ** -5
        ),
        'pounds per square inch': props(
            quantity='pressure',
            name='pounds per square inch',
            symbol='psi',
            base='pascal',
            to_base=lambda x: 6.8948 * x * 10 ** 3,
            from_base=lambda x: 1.450377 * x * 10 ** -4
        ),
    }

    # Dimensionless Units
    dimensionless = {
        'dimensionless': props(
            quantity='dimensionless',
            name='-',
            symbol='-',
            base='-',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'percentage': props(
            quantity='dimensionless',
            name='percent',
            symbol='percent',
            base='dimensionless',
            to_base=lambda x: x * 10 ** -2,
            from_base=lambda x: x * 10 ** 2
        ),
    }

    # Undefined Units
    undefined = {
        'undefined': props(
            quantity='undefined',
            name='undef',
            symbol='undef',
            base='undef',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
    }

    # Units of Length
    length = {
        'meter': props(
            quantity='length',
            name='meter',
            symbol='m',
            base='meter',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'inch': props(
            quantity='length',
            name='inch',
            symbol='in',
            base='meter',
            to_base=lambda x: 0.0254 * x,
            from_base=lambda x: x / 0.0254
        ),
        'foot': props(
            quantity='length',
            name='inch',
            symbol='ft',
            base='meter',
            to_base=lambda x: 0.3048 * x,
            from_base=lambda x: x / 0.3048
        ),
        'yard': props(
            quantity='length',
            name='inch',
            symbol='yd',
            base='meter',
            to_base=lambda x: 0.9144 * x,
            from_base=lambda x: x / 0.9144
        ),
        'mile': props(
            quantity='length',
            name='inch',
            symbol='mi',
            base='meter',
            to_base=lambda x: 1609.344 * x,
            from_base=lambda x: x / 1609.344
        ),
    }

    # Units of Mass
    mass = {
        'gram': props(
            quantity='mass',
            name='gram',
            symbol='g',
            base='gram',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'tonne': props(
            quantity='mass',
            name='tonne',
            symbol='t',
            base='g',
            to_base=lambda x: 1000E3 * x,
            from_base=lambda x: x / 1000E3
        ),
        'slug': props(
            quantity='mass',
            name='slug',
            symbol='sl',
            base='g',
            to_base=lambda x: 14594 * x,
            from_base=lambda x: x / 14594
        ),
        'pound (mass)': props(
            quantity='mass',
            name='pound (mass)',
            symbol='lbm',
            base='g',
            to_base=lambda x: 453.6 * x,
            from_base=lambda x: x / 453.6
        ),
    }

    # Units of time
    time = {
        'second': props(
            quantity='time',
            name='second',
            symbol='s',
            base='s',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
        'minute': props(
            quantity='time',
            name='minute',
            symbol='min',
            base='s',
            to_base=lambda x: 60. * x,
            from_base=lambda x: x / 60.
        ),
        'hour': props(
            quantity='time',
            name='hour',
            symbol='hr',
            base='s',
            to_base=lambda x: 3600. * x,
            from_base=lambda x: x / 3600.
        ),
        'day': props(
            quantity='time',
            name='day',
            symbol='d',
            base='s',
            to_base=lambda x: 86400. * x,
            from_base=lambda x: x / 86400.
        ),
        'year': props(
            quantity='time',
            name='year',
            symbol='yr',
            base='s',
            to_base=lambda x: 365. * 24. * 60. * 60. * x,
            from_base=lambda x: x / (365. * 24. * 60. * 60.)
        ),
    }

    # Units of electric current
    current = {
        'ampere': props(
            quantity='electric current',
            name='ampere',
            symbol='A',
            base='A',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
    }

    # Units of electric potential
    voltage = {
        'voltage': props(
            quantity='electric potential',
            name='voltage',
            symbol='V',
            base='V',
            to_base=BASE_TO_BASE,
            from_base=BASE_TO_BASE
        ),
    }

    library = dict(
        list(temperature.items()) +
        list(pressure.items()) +
        list(dimensionless.items()) +
        list(undefined.items()) +
        list(length.items()) +
        list(mass.items()) +
        list(time.items()) +
        list(current.items()) +
        list(voltage.items())
    )

    return library
