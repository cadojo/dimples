"""
Specifications, and parsers for Python project metadata files (pyproject.toml), and 
manifest files (pyproject.lock).
"""

import typing, dataclasses, abc

from . import validate


class ProjectFile(abc.ABC):
    """
    All subclasses will have a file attribute, a data attribute, and a default constructor
    which blindly loads the file.
    """

    @abc.abstractmethod
    def isvalid(cls) -> bool:
        """
        Returns True if the underlying data matches the file type's specification.
        """

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


@dataclasses.dataclass
class ProjectMetadata(ProjectFile):
    """
    A simple type to abstract a project's metadata contained within pyproject.toml. Provides
    a __post_init__ method which validates the provided file.
    """

    def isvalid(self):
        from .validate import metadata

        return metadata(self.data)

    def __init__(self, file: str, /):
        """
        Load the provided metadata file.
        """
        super().__init__(file)


@dataclasses.dataclass
class ProjectManifest(ProjectFile):
    """
    A simple type to abstract a project's manifest contained within pyproject.lock. Provides
    a __post_init__ method which validates the provided file.
    """

    def isvalid(self):
        from .validate import manifest

        return manifest(self.data)

    def __init__(self, file: str, /):
        """
        Load the provided manifest file.
        """
        super().__init__(file)


del dataclasses, typing
