"""
Abstract interfaces for Python package servers.
"""

__export__ = {
    "PackageServer",
    "ServerAPI",
}

from enum import Enum, auto
from typing import Protocol, Optional


class PackageServer(Enum):
    """
    All package server types supported by `pkg`!
    """

    PyPI = auto()


class ServerAPI(Protocol):
    """
    An abstract interface for all Python package servers.
    """

    def __distribution__(self, package: str, /, *, version: Optional[str]) -> str:
        """
        Returns the URL associated with the requested package distribition.
        """

    def __versions__(self, package: str, /) -> set[str]:
        """
        Return the set of all versions for the provided package.
        """

    def __download__(
        self, package: str, /, *, location: str, version: Optional[str]
    ) -> None:
        """
        Download the distribution for the specified package, and optionally specified
        version, to some location. If no version is provided, the largest version number
        found on the server should be used.
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
