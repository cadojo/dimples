"""
Interfaces and implementations for Python package registries.
"""

import typing
import dataclasses

from ..protocols.registries import PythonRegistry


def alias(registry: PythonRegistry, /):
    """
    Return the alias of the provided registry.
    """
    return registry.__alias__()


def index(registry: PythonRegistry, /):
    """
    Return the index URL of the provided registry.
    """
    return registry.__index__()


def private(registry: PythonRegistry, /):
    """
    Returns True if the index URL is not publicly accessible, or if the index is otherwise
    not intended for public use.
    """
    return registry.__private__()


@dataclasses.dataclass(kw_only=True)
class Registry:
    """
    An implementation for a Python package registry.
    """

    url: str = dataclasses.field()
    alias: str = dataclasses.field()
    private: bool = dataclasses.field()

    def __alias__(self) -> str:
        """
        Return the alias of the registry.
        """
        return self.alias

    def __private__(self) -> bool:
        """
        Returns False if the registry is publicly accessible.
        """
        return self.private

    def __index__(self) -> str:
        """
        Return the index associated with the registry.
        """
        return self.url


del dataclasses, typing, PythonRegistry
