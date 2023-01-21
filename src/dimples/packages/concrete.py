"""
Interact with Python packages, and make sure to store where they came from!
"""

from __future__ import annotations as __annotations

__export__ = {
    "Package",
}

import dataclasses, typing
from ..registries.abstract import PythonRegistry


@dataclasses.dataclass(kw_only=True)
class Package:
    """
    A representation for a Python package.
    """

    name: str = dataclasses.field(kw_only=False)
    version: str = dataclasses.field(default="")
    dependencies: typing.Set[Package] = dataclasses.field(default_factory=set)
    registry: str = dataclasses.field(default="pypi")

    def __name__(self):
        """
        Return the package name.
        """
        return self.name

    def __version__(self):
        """
        Return the package version.
        """
        return self.version

    def __registry__(self):
        """
        Return the registry from which this package should be installed.
        """
        return self.registry

    def __dependencies__(self):
        """
        Return each explicitly defined dependency.
        """
        return self.dependencies


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
