"""
Specifications, and parsers for Python project metadata files (pyproject.toml), and 
manifest files (pyproject.lock).
"""

import typing, dataclasses


@dataclasses.dataclass
class ProjectDependency:

    name: str = dataclasses.field(hash=True)
    version: str = dataclasses.field(hash=True)
    by: typing.Set[str] = dataclasses.field(hash=False)


@dataclasses.dataclass
class ProjectMetadata:
    """
    A simple type to abstract a project's metadata contained within pyproject.toml. Provides
    a __post_init__ method which validates the provided file.
    """

    @classmethod
    def isvalid(cls, data: dict[str, typing.Any]) -> bool:
        """
        Returns True if the underlying data matches the file type's specification.
        """
        from . import validate

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
        return [dependency for dependency in self.project["dependencies"]]

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


@dataclasses.dataclass
class ProjectManifest:
    """
    A simple type to abstract a project's manifest contained within pyproject.lock. Provides
    a __post_init__ method which validates the provided file.
    """

    def isvalid(cls, data: dict[str, typing.Any]) -> bool:
        """
        Returns True if the underlying data matches the file type's specification.
        """
        from . import validate

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
    def requirements(self):
        """
        Return the contents of the [requirements] key, if it exists.
        Otherwise, return an empty set.
        """
        return {requirement for requirement in self.data.get("requirements", set())}

    @property
    def dependencies(self):
        """
        Return every dependency required for this frozen dependency set.
        """
        return {dependency for dependency in self.data.get("dependencies", set())}

    def resolve(
        self,
    ) -> typing.Dict[ProjectDependency, typing.Set[ProjectDependency]]:
        """
        Resolve the environment into a replicable build.
        """
        ...


del dataclasses, typing
