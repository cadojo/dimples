"""
Abstract interfaces for Python package registries.
"""


__export__ = {
    "PythonRegistry",
}

from typing import Protocol, Optional


class PythonRegistry(Protocol):
    """
    An abstract interface for Python registries.
    """

    def __alias__(self) -> str:
        """
        Return the alias of the registry.
        """

    def __index__(self) -> str:
        """
        Return the URL of the registry.
        """

    def __private__(self) -> bool:
        """
        Returns False if the registry is publicly accessible.
        """


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
