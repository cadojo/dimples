"""
Interfaces and implementations for Python package registries.
"""

from . import abstract, concrete


def alias(registry: abstract.PythonRegistry, /):
    """
    Return the alias of the provided registry.
    """
    return registry.__alias__()


def index(registry: abstract.PythonRegistry, /):
    """
    Return the index URL of the provided registry.
    """
    return registry.__index__()


def private(registry: abstract.PythonRegistry, /):
    """
    Returns True if the index URL is not publicly accessible, or if the index is otherwise
    not intended for public use.
    """
    return registry.__private__()
