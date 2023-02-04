"""
Abstract interfaces for all Python packages.
"""

from __future__ import annotations as __annotations

__export__ = {
    "PythonPackage",
}

from typing import Protocol, Set
from .registries import PythonRegistry


class PythonPackage(Protocol):
    """
    An abstract interface for any type which describes a Python package!
    """

    def __name__(self) -> str:
        """
        Return the install-able name of the package.
        """

    def __version__(self) -> str:
        """
        Return the version to install, or the version that is installed!
        """

    def __registry__(self) -> PythonRegistry:
        """
        Returns the URL associated with the registry from which the package was installed.
        """

    def __dependencies__(self) -> Set[PythonPackage]:
        """
        Return the set of all PythonPackage dependencies. Note this set is NOT flat! Each
        dependency may have its own set of dependencies, and so on.
        """


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
