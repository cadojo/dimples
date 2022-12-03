"""
Implementations for Python indices and registries.
"""

__export__ = {
    "Registry",
}

from typing import NamedTuple
from .types.servers import PackageServer


class Registry(NamedTuple):
    """
    A generic implementation for a Python registry.
    """

    alias: str
    url: str
    public: bool
    api: PackageServer = PackageServer.PyPI

    def update(self) -> None:
        """
        Fetch the latest package metadata changes from the registry.
        """

    def __alias__(self):
        """Return the alias of the registry."""
        return self.alias
