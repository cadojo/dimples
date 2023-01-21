"""
Abstract interfaces for Python environments with index-specification!
"""

__export__ = {
    "PythonEnvironment",
}

from typing import Protocol, Dict, Set
from ..packages.abstract import PythonPackage
from ..registries.abstract import PythonRegistry


class PythonEnvironment(Protocol):
    """
    An abstract interface for a Python environment.
    """

    def __environment__(self) -> str:
        """
        Returns the base path associated with the environment. There must be at least a
        metadata file (pyproject.toml) at this path. A manifest file will be created at this
        path, if the "dimples" package manager is used.
        """

    def __update__(self, *packages: str, cautious: bool = False, **kwargs) -> None:
        """
        Update every package in the environment. If cautious is set to False, an "eager"
        update style is applied, and every package dependency is also checked for
        update-ability.
        """

    def __metadata__(self) -> Set[PythonPackage]:
        """
        Return the set of explicitly installed Python packages.
        """

    def __manifest__(self) -> Dict[PythonPackage, Set[PythonPackage]]:
        """
        Return the set of all installed Python packages (explicitly, or implicitly).
        """


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
