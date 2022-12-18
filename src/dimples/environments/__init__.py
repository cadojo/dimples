"""
Interact with Python environments.
"""

__export__ = {
    "update",
    "packages",
    "manifest",
    "registries",
    "PythonEnvironment",
    "REQUIRED_FILE",
    "MANIFEST_FILE",
}

from typing import Protocol, Literal
from ..packages import PythonPackage
from ..registries import PythonRegistry


class PythonEnvironment(Protocol):
    """
    An abstract interface for a Python environment.
    """

    def __environment__(self) -> str:
        """
        Returns the base path associated with the environment.
        """

    def __update__(self, *packages: str, cautious: bool = False) -> None:
        """
        Update every package in the environment. If cautious is set to False, an "eager"
        update style is applied, and every package dependency is also checked for
        update-ability.
        """

    def __registries__(self) -> set[PythonRegistry]:
        """
        Return all available registires added to this environment.
        """

    def __required__(self) -> set[PythonPackage]:
        """
        Return the set of explicitly installed Python packages.
        """

    def __manifest__(self) -> set[PythonPackage]:
        """
        Return the set of all installed Python packages (explicitly, or implicitly).
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
