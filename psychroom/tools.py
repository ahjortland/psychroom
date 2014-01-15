"""Useful tools when dealing with Test Data Frames."""


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
        return {key: val for key, val in units.items() if key in keys}
    else:
        return units


def descriptions(self, keys=None):
    """Return a dictionary of a description of each column in dataframe.

    Parameters
    ----------
    key : column name string
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
