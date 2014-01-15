"""Utility functions used for working with sensor measurment data."""

from os import path

from compat import PY3

if PY3:
    from configparser import SafeConfigParser
else:
    from ConfigParser import SafeConfigParser


def load_library(filepath):
    """Load sensor label configuration file.

    Parameters
    ----------
    filepath : string

    Returns
    -------
    library : SafeConfigParser

    """

    parser = SafeConfigParser()
    parser.read(filepath)

    sections = ['components', 'fluids', 'locations', 'measurement types']

    missing = set(sections) - set(parser.sections())

    if missing:
        print('Found sections: ', sorted(parser.section()))
        print('Missing sections: ', sorted(missing))

    return parser


def translate_label(label, library=None, sep='_'):
    """Translate a sensor measurement label to pretty description.

    Parameters
    ----------
    label : string
        Measurement label string formatted using the Herrick
        Psychrometric Chamber Experimental Data Standard
    library : SafeConfigParser
        Sensor label translator dictionary for components, fluids,
        locations, and measurement types parts of the sensor
        measurement label.
    sep : string, optional, default '_'
        Separator character used in measurement label, optional
        parameter should only be used in special cases when default
        value, '_', cannot be used.

    Returns
    -------
    description : string if parsing succeeded
        formatted descriptive string of measurement label, useful if not
        familiar with the labelling convention

    Examples
    --------
    >>> translate_label('comp_ref_in_T')
    'compressor refrigerant inlet temperature'

    >>> translate_label('ahu/air/mix/RH', sep='/')
    'air handling unit air mixed relative humidity'

    """

    if not library:
        library = load_library(path.abspath('./defaults.ini'))

    SECTIONS = ('components', 'fluids', 'locations', 'measurement types')

    description = ' '.join([
        library.get(sec, abrv) for sec, abrv in zip(SECTIONS, label.split(sep))
    ])

    return description


def translate_keys(df, keys=None):
    """Add a label translation for keys in a data frame.

    Parameters
    ----------
    df : pandas DataFrame
        data frame object containing measurement data with keys
        formatted using the Herrick Pyschrometric Chamber Experimental
        Data Standard.
    keys : [string]
        list of label strings contained in the measurement data frame
        translated into descriptions.

    Returns
    -------
    df : pandas DataFrame
        data frame object updated with a new 'description' property
        added to columns corresponding to the keys parameter.

    """

    for key in keys:
        df[key]._descriptions = translate_label(key)

    return df
