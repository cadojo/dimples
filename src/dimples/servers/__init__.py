"""
Abstract interfaces for Python package servers.
"""

__export__ = {
    "PackageServer",
    "ServerAPI",
    "distribution",
    "versions",
    "download",
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


def distribution(
    server: PackageServer, /, package: str, *, version: Optional[str] = None
) -> str:
    """
    Return the URL associated with the requested package distribution.
    """
    return server.__distribution__(package, version=version)


def versions(server: PackageServer, /, package: str) -> set[str]:
    """
    Return the set of all versions for the provided package.
    """
    return server.__versions__(package)


def download(
    server: PackageServer,
    /,
    package: str,
    *,
    location: str = curdir,
    version: Optional[str] = None,
) -> None:
    """
    Download the requested package, and optionally specified version, to some location. If no version is provided,
    the largest version number found on the server will be used.
    """
    return server.__download__(package, location=location, version=version)


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
