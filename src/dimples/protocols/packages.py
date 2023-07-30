"""
Abstract interfaces for all Python packages.
"""

from __future__ import annotations as __annotations

__export__ = {
    "PythonPackage",
}

from typing import Protocol
from packaging.version import Version
from uuid import UUID

from .manifests import ProjectManifest
from .metadata import ProjectMetadata


class PythonPackage(Protocol):
    """
    An abstract interface for any type which describes a Python package!
    """

    def __name__(self) -> str:
        """
        Return the install-able name of the package.
        """

    def __version__(self) -> Version:
        """
        Return the version to install, or the version that is installed!
        """

    def __uuid__(self) -> UUID:
        """
        Returns the URL associated with the registry from which the package was installed.
        """

    def __update__(self, *packages: str, cautious: bool = False, **kwargs) -> None:
        """
        Update every package in the environment. If cautious is set to False, an "eager"
        update style is applied, and every package dependency is also checked for
        update-ability.
        """

    def __metadata__(self) -> ProjectMetadata:
        """
        Return the set of explicitly installed Python packages.
        """

    def __manifest__(self) -> ProjectManifest:
        """
        Return the set of all installed Python packages (explicitly, or implicitly).
        """


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
