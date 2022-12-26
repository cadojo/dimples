"""
Abstract interfaces for all Python packages.
"""

__export__ = {
    "PythonPackage",
}

from typing import Protocol, Optional
from ..registries.protocols import PythonRegistry


class PythonPackage(Protocol):
    """
    An abstract interface for any type which describes a Python package!
    """

    def __package__(self) -> str:
        """
        Return the install-able name of the package.
        """

    def __uuid__(self) -> Optional[str]:
        """
        Returns the UUID of the package, if one exists.
        """

    def __registry__(self) -> PythonRegistry:
        """
        Returns the URL associated with the registry from which the package was installed.
        """

    def __version__(self) -> str:
        """
        Returns the version specifier for this package.
        """



if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
