"""
Interfaces and implementations for environment manifests.
"""


import dataclasses, typing
from ...packages import Package


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
        from ..toml import load

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
    def dependencies(self):
        """
        Return the contents of the [dependencies] key, if it exists.
        Otherwise, return an empty set.
        """
        from ...packages import Package

        return {
            Package.from_dict(dependency)
            for dependency in self.data.get("dependencies", set())
        }

    def status(
        self,
    ) -> typing.Dict[Package, typing.Set[Package]]:
        """
        Resolve the environment into a replicable build.
        """
        return {
            Package.from_dict(dependency): {
                Package.from_dict(by) for by in dependency.get("by", set())
            }
            for dependency in self.dependencies
        }


del dataclasses, typing
