# -*- coding: utf-8 -*-
"""Utility functions and variables used throughout code."""

from .compat import PY3


if PY3:
    DEG_SYMBOL = u'\u00B0'  # this symbol -> ° as unicode
    MICRO_SYMBOL = u'\u00B5'
else:
    DEG_SYMBOL = 'deg'
    MICRO_SYMBOL = 'u'
