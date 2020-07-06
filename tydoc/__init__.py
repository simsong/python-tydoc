# encoding: utf-8

"""Initialization module for python-tydoc package."""

__version__ = "0.1.0"

import tydoc.exceptions as exceptions
import sys

sys.modules["tydoc.exceptions"] = exceptions
del sys

