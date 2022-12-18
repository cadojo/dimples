"""
Interfaces and implementations for a user-facing package manager.
"""

__export__ = {
    "PackageManager",
}

from packaging.version import Version
from typing import Protocol, Optional, Mapping
from ..packages import PythonPackage
from ..environments import PythonEnvironment


class PackageManager(Protocol):
    """
    An abstract interface for all user-facing Python package managers.
    """

    def __active__(self) -> PythonEnvironment:
        """
        Return the currently active python environment.
        """

    def __install__(
        self,
        package: str,
        /,
        version: Optional[str] = None,
        *,
        index: Optional[str] = None,
    ):
        """
        Add the specified package to the active environment.
        """

    def __uninstall__(self, package: str):
        """
        Uninstall the specified package from the active environment.
        """

    def __update__(self, *packages: str, cautious: bool = False):
        """
        Update each provided package. If no packages are provided, the full environment is
        updated. An eager update strategy is used by default; this can be disabled by
        setting cautious to True.
        """

    def __active__(
        self,
    ) -> str:
        """
        Return the name of the currently active environment.
        """

    def __status__(
        self, *packages: str, indirect: bool = False
    ) -> Mapping[PythonPackage, Version]:
        """
        Return a map from each installed package to its version. If indirect is set to True,
        all installed packages will be included. Otherwise, only directly installed
        dependencies are shown.
        """

    def __resolve__(self):
        """
        Resolve all dependencies in the active environment's metadata file, and update the
        environment's manifest file accordingly.
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
