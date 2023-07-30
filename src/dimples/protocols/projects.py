"""
Abstract interfaces for all Python projects: packages, and environments.
"""

from __future__ import annotations as __annotations

__export__ = {
    "PythonProject",
}

from typing import Protocol
from .registries import PythonRegistry
from .metadata import ProjectMetadata
from .manifests import ProjectManifest

class PythonProject(Protocol):
    """
    An abstract interface for any type which describes a Python project!
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
