"""
Interact with Python packages, and make sure to store where they came from!
"""

import dataclasses, typing
from ..registries.protocols import PythonRegistry


class RegistryField(typing.TypedDict):
    """
    A type alias which provides types for each individual registry field.
    """

    alias: str
    url: str
    uuid: str


class MetadataDict(typing.TypedDict):
    """
    A type alias which provides types for each individual metadata value.
    """

    name: str
    version: str
    registry: RegistryField
    uuid: typing.Optional[str]


@dataclasses.dataclass(frozen=True)
class Package:
    """
    A representation for a Python package.
    """

    name: str = dataclasses.field()
    version: str = dataclasses.field()
    registry: PythonRegistry = dataclasses.field()
    uuid: typing.Optional[str] = dataclasses.field()

    def __package__(self):
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

    def __uuid__(self):
        """
        Return the UUID, if one exists, for this package.
        """
        return self.uuid

    @classmethod
    def from_dict(cls, dependency: MetadataDict):
        """
        Construct a Package from a dictionary.
        """
        from ..configuration import registry
        from typing import Optional

        name: str = dependency["name"]
        version: str = dependency["version"]
        uuid = dependency["uuid"]
        if uuid == "":
            uuid = None

        reg = registry(**dependency.get("registry", {}))

        return cls(name=name, version=version, registry=reg, uuid=uuid)


del dataclasses, typing, PythonRegistry
