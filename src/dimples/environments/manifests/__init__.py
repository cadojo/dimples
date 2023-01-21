"""
Interfaces and implementations for environment manifests.
"""


import dataclasses, typing
from ...packages.concrete import Package
from ...packages.abstract import PythonPackage


@dataclasses.dataclass
class Manifest:
    """
    A simple type to abstract a project's manifest contained within pyproject.lock. Provides
    a __post_init__ method which validates the provided file.
    """

    def isvalid(cls, data: dict[str, typing.Any]) -> bool:
        """
        Returns True if the underlying data matches the file type's specification.
        """
        from .. import validate

        return validate.manifest(data)

    file: str = dataclasses.field(hash=True)
    data: dict[str, typing.Any] = dataclasses.field(hash=False)

    def __init__(self, file: str, /):
        """
        Load the provided metadata file.
        """
        from ...toml import load

        with open(file, "rb") as stream:
            self.data = load(stream)

        self.file = file

    def __post_init__(self):
        """
        Validate the data loaded by the __init__ method.
        """
        if not self.isvalid(self.data):
            raise ValueError(f"The data provided by {self.file} is invalid!")

    @property
    def metadata(self):
        """
        Return the contents of the [metadata] key.
        """
        return self.data["metadata"]

    @property
    def dependencies(self) -> typing.Dict[PythonPackage, typing.Set[PythonPackage]]:
        """
        Return the contents of the [dependencies] key, if it exists.
        Otherwise, return an empty set.
        """
        from ...packages.concrete import Package

        return {
            Package.from_dict(dependency): {
                Package.from_dict(subdependency) for subdependency in dependency["by"]
            }
            for dependency in self.data.get("dependencies", set())
        }

    def status(
        self,
    ) -> typing.Dict[Package, typing.Set[Package]]:
        """
        Resolve the environment into a replicable build.
        """
        from typing import cast
        from ..metadata.protocols import MetadataDict

        return {
            Package.from_dict(dependency): {
                Package.from_dict(cast(MetadataDict, by))
                for by in dependency.get("by", set())
            }
            for dependency in self.data["dependencies"]
        }

    def __file__(self) -> typing.Optional[str]:
        """
        Return the manifest file, if one exists. Otherwise, return None.
        """
        return self.file

    def __metadata__(self) -> typing.Dict[str, str]:
        """
        Parse the manifest file for the manifest metadata, and return the resulting dictionary.
        """
        return self.metadata

    def __dependencies__(self) -> typing.Dict[PythonPackage, typing.Set[PythonPackage]]:
        """
        Parse the manifest file for the manifest data, and return the resulting dictionary.
        """
        return self.dependencies


del dataclasses, typing
