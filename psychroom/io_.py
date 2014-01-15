"""Experimental data input/output handler functions."""
# TODO Uncertainty
from collections import namedtuple
import os
from os.path import join

import pandas as pd

from label_handler import translate_keys
from unit import Unit
from compat import (casefold, filter, isdecimal, isidentifier)
from frames import monkey_patch

monkey_patch()


def load_(filepath, ext='.htf', **kwargs):
    """Load a collection of test data and return pandas DataFrames.

    Parameters
    ----------
    filepath : str
        directory containing experimental data files

    Returns
    -------
    data : {pandas DataFrame}
        dictionary of all the data in each test file as data frames
    summary : pandas DataFrame
        a summary data frame of the data from all the test files

    """

    is_ext = lambda s: True if s.endswith(ext) else False

    for root, _, files in os.walk(filepath):
        data = {
            ind: read_(join(root, f), **kwargs)
            for ind, f in enumerate(filter(is_ext, sorted(files)))
        }

    summary = pd.DataFrame(
        data={name: item.mean() for name, item in data.items()}
    ).T
    for key in summary.keys():
        summary[key]._units = data[0][key]._units
    for id_, _ in summary.iterrows():
        for section, metadata in data[id_].metadata.items():
            for key, info in metadata.items():
                if key in summary.keys():
                    summary[key][id_], summary[key]._units = info
                else:
                    summary[key] = info.value
                    summary[key]._units = info.unit

    return data, summary


def read_(filepath_or_buffer, header=0, units=1, **kwargs):
    """Read experimental data into pandas DataFrame.

    Parameters
    ----------
    filepath_or_buffer : string or file handle / StringIO.

    header : int
        Row to use for the column labels of the parsed DataFrame.
    units : int
        Row to use for the unit properties of the parsed DataFrame.

    Returns
    -------
    result : pandas DataFrame

    """

    with open(filepath_or_buffer, 'r') as f:
        metadata = parse_metadata(f)
        result = parse_raw_data(f, **kwargs)

    result = append_metadata(result, metadata)

    # Currently, pandas only copies attributes that are added to
    # _metadata when it is copied.  Since pandas actually copies
    # frames frequently, this is a problem. To get around this, use
    # monkey-patching to store frame attributes and methods.
    result._metadata.append('_units')  # unit dictionary
    result._metadata.append('_descriptions')  # description dictionary

    return result


def parse_metadata(handle):
    """Parse test data file header metadata.

    Parameters
    ----------
    handle : test data file handle

    Returns
    -------
    metadata : dict
        parsed metadata dictionary describing test procedure

    """

    MetadataInfo = namedtuple('MetadataInfo', ['value', 'unit'])

    metadata = {}
    while True:
        line = handle.readline().strip()
        if line.startswith('[raw data]'):
            return metadata
        elif line.startswith('[') and line.endswith(']'):
            section = cleanse_names(line.strip().strip('[]'))
            metadata[section] = {}
        else:
            key, info = [item.strip() for item in line.split('=')]
            key = cleanse_names(key)
            value, unit = parse_metadata_info(info)
            metadata[section][key] = MetadataInfo(*parse_metadata_info(info))


def parse_metadata_info(info):
    """Parse floating point metadata info.

    Parameters
    ----------
    info : string

    Returns
    -------
    value : float
    unit : string

    """
    value, _, unit = [item.strip() for item in info.partition('[')]
    unit = unit.strip('[]') if unit else None

    # TODO Not happy with this code, don't like logic trees in general.
    # Also, I think there is many oppurtunities for Exceptions, should
    # make this more robust.
    if unit:
        if casefold(unit) == 'bool':
            value = True if casefold(value) == 'true' else False
        elif value.isdigit():
            value = int(value)
        elif isdecimal(value.replace('.', '')):
            unit = Unit(unit)
            value = float(value)

    return value, unit


def parse_raw_data(handle, **kwargs):
    """Parse raw data from test output data file.

    Parameters
    ----------
    handle : test data file handle

    Returns
    -------
    result : pandas DataFrame

    """

    read_col_metadata = lambda line: line.strip().split(',')[1:]

    column_names = cleanse_names(read_col_metadata(handle.readline()))
    column_units = read_col_metadata(handle.readline())
    result = pd.read_csv(handle, names=column_names, **kwargs)

    # TODO It would be cool if key-unit pairs were methods that updated
    # with each call.
    for key, unit in zip(result.keys(), column_units):
        result[key]._units = Unit(unit)
    result._units = {key: result[key]._units for key in result.keys()}

    result = translate_keys(result, result.keys())
    result._descriptions = {
        key: result[key]._descriptions for key in result.keys()
    }

    return result


def cleanse_names(names, bad_chars=[], repl='_'):
    """Cleanse a list of proposed column names to correct format.

    Parameters
    ----------
    names : string or [string]
        A string or list of proposed DataFrame column name strings
        usually read from test data file raw data header or metadata
        information.
    bad_chars : [string]
        List of invalid or bad characters that should be replaced from
        name strings if present
    repl : string
        String replacement for bad characters in cleansed name strings.

    Returns
    -------
    result : string or [string]
        String or list of cleansed DataFrame column names.

    Examples
    >>> cleanse_names(['a b c d', 'e_f g_i', 'j_k'])
    ['a_b_c_d', 'e_f_g_i', 'j_k']

    >>> cleanse_names(['1abc0'], repl='_')
    ['_abc0']

    >>> cleanse_names(' xxx')
    '_xxx'

    >>> cleanse_names('abcdef')
    'abcdef'

    """

    clean = lambda x, y: x + y if isidentifier(x + y) else x + repl

    result = ''
    if isinstance(names, str):
        for char in names:
            result = clean(result, char)
    else:
        result = [result] * len(names)
        for ind, name in enumerate(names):
            for char in name:
                result[ind] = clean(result[ind], char)

    return result


def append_metadata(data, metadata):
    """Append metadata information to the measurement DataFrame.

    Parameters
    ----------
    data : pandas DataFrame
        measurement DataFrame associated with metadata.
    metadata : dict
        metadata dictionary usually parsed from test data file header.

    Returns
    -------
    result : pandas DataFrame
        measurement DataFrame containing additional metadata properties.

    """

    data.metadata = metadata
    for section, meta in metadata.items():
        data.__dict__[section] = pd.DataFrame(
            {key: [info.value] for key, info in meta.items()}
        )
        for key, info in meta.items():
            data.__dict__[section][key]._units = info.unit

    return data
