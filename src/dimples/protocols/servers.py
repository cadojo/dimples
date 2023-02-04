"""
Abstract interfaces for Python package servers.
"""

__export__ = {
    "PackageServer",
}

from os.path import curdir
from enum import Enum, auto
from typing import Protocol, Optional


class ServerAPI(Enum):
    """
    All package server types supported by `pkg`!
    """

    PyPI = auto()
    Repository = auto()


class PackageServer(Protocol):
    """
    An abstract interface for all Python package servers.
    """

    def __distribution__(
        self, package: str, /, *, version: Optional[str] = None
    ) -> str:
        """
        Returns the URL associated with the requested package distribution.
        """

    def __packages__(self) -> set[str]:
        """
        Return the full set of packages available on the server.
        """

    def __versions__(self, package: str, /) -> set[str]:
        """
        Return the set of all versions for the provided package.
        """

    def __download__(
        self,
        package: str,
        /,
        *,
        location: str = curdir,
        version: Optional[str] = None,
    ) -> None:
        """
        Download the distribution for the specified package, and optionally specified
        version, to some location. If no version is provided, the largest version number
        found on the server will be used.
        """


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
