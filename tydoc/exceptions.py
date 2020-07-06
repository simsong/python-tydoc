# encoding: utf-8

"""
Exceptions used with python-tydoc.

The base exception class is PythonTydocError.
"""


class PythonTydocError(Exception):
    """Generic error class."""


class PackageNotFoundError(PythonTydocError):
    """
    Raised when a package cannot be found at the specified path.
    """


class InvalidXmlError(PythonTydocError):
    """
    Raised when a value is encountered in the XML that is not valid according
    to the schema.
    """
