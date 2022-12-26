"""
Interact with Python packages, and make sure to store where they came from!
"""

import dataclasses, typing
from ..registries.protocols import PythonRegistry


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
    def from_dict(
        cls, dependency: typing.Dict[str, typing.Union[str, typing.Dict[str, str]]]
    ):
        """
        Construct a Package from a dictionary.
        """
        from ..registries import Registry

        name: str = dependency["name"]
        version: str = dependency["version"]
        registry = Registry(**dependency["registry"])
        uuid = dependency.get("uuid", None)
        if uuid == "":
            uuid = None

        return cls(name=name, version=version, registry=registry, uuid=uuid)


del dataclasses, typing, PythonRegistry
