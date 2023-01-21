"""
Abstract interfaces for environment metadata files.
"""

__export__ = {
    "ToolDict",
    "ToolDimplesDict",
    "ToolDimplesProjectDict",
    "ProjectDict",
    "MetadataDict",
    "ProjectMetadata",
}

from typing_extensions import NotRequired
from typing import Protocol, Optional, Dict, TypedDict, List
from ...projects import ProjectType


class ToolDimplesProjectDict(TypedDict):
    """
    A type alias for dictionary representations of the [tool.dimples.project] key in a
    metadata file.
    """

    uuid: str
    type: str


class ToolDimplesDict(TypedDict):
    """
    A type alias for dictionary representations of the [tool.dimples] key in a metadata file.
    """

    project: ToolDimplesProjectDict


class ToolDict(TypedDict):
    """
    A type alias for dictionary representations of the [tool.dimples] key in a metadata file.
    """

    dimples: ToolDimplesDict


class ProjectDict(TypedDict):
    """
    A type alias for dictionary representations of the project key in a metadata file.
    """

    name: str
    version: str
    dependencies: List[str]
    dynamic: NotRequired[List[str]]


class MetadataDict(TypedDict):
    """
    A type alias for a dictionary representation of the metadata file.
    """

    project: ProjectDict
    tool: ToolDict


class ProjectMetadata(Protocol):
    """
    An abstract interface for all metadata files.
    """

    def __file__(self) -> Optional[str]:
        """
        Return the metadata file, if one exists. Otherwise, return None.
        """

    def __project__(self) -> ProjectDict:
        """
        Parse the manifest file for the project metadata, and return the resulting dictionary.
        Project "type" and "uuid", which are held under [tool.dimples], should also be available
        as top-level keys in the dictionary.
        """

    def __type__(self) -> ProjectType:
        """
        Return the type of the project defined by the metadata file.
        """

    def __uuid__(self) -> Optional[str]:
        """
        Return the UUID of the project, if one exists. Otherwise, return None.
        """

    def __version__(self) -> str:
        """
        Return the version for the project.
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
