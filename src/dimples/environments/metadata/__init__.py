"""
Interfaces and implementations for environment metadata.
"""

"""
Specifications, and parsers for Python project metadata files (pyproject.toml), and 
manifest files (pyproject.lock).
"""

import typing, dataclasses
from ...packages import Package
from ...projects import ProjectType


@dataclasses.dataclass
class Metadata:
    """
    A simple type to abstract a project's metadata contained within pyproject.toml. Provides
    a __post_init__ method which validates the provided file.
    """

    @classmethod
    def isvalid(cls, data: dict[str, typing.Any]) -> bool:
        """
        Returns True if the underlying data matches the file type's specification.
        """
        from .. import validate

        return validate.metadata(data)

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
    def project(self):
        """
        Return the contents of the [project] key.
        """
        return self.data["project"]

    @property
    def dependencies(self):
        """
        Return the contents of the [project.dependencies] key.
        """
        return {dependency for dependency in self.project["dependencies"]}

    @property
    def extras(self):
        """
        Return the contents of the [project.optional-dependencies] key, if it exists.
        Otherwise, return an empty dictionary.
        """
        return {
            extra: dependencies
            for (extra, dependencies) in self.project.get("optional-dependencies", {})
        }

    def __file__(self) -> typing.Optional[str]:
        """
        Return the manifest file, if one exists. Otherwise, return None.
        """
        return self.file

    def __project__(self) -> typing.Dict[str, str]:
        """
        Parse the manifest file for the project metadata, and return the resulting dictionary.
        Project "type" and "uuid", which are held under [tool.dimples], should also be available
        as top-level keys in the dictionary.
        """
        return self.project

    def __type__(self) -> ProjectType:
        """
        Return the type of the project defined by the metadata file.
        """
        from ...projects import ProjectType

        return ProjectType.from_str(self.data["tool"]["dimples"]["type"])

    def __uuid__(self) -> typing.Optional[str]:
        """
        Return the UUID of the project, if one exists. Otherwise, return None.
        """
        try:
            uuid = self.data["tool"]["dimples"]["uuid"]
        except KeyError:
            uuid = None

        return uuid if uuid else None

    def __version__(self) -> str:
        """
        Return the version for the project.
        """
        try:
            return self.project["version"]
        except KeyError:
            try:
                if "version" in self.project["dynamic"]:
                    raise NotImplementedError()
                else:
                    raise ValueError("Invalid metadata state!")
            except KeyError:
                raise ValueError("Invalid metadata state!")


del dataclasses, typing, Package
