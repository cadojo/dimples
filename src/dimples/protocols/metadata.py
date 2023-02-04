"""
Abstract interfaces for environment metadata files.
"""

__export__ = {
    "ProjectMetadata",
    "MetadataContents",
}

from packaging.requirements import Requirement
from typing import Protocol, Optional, Set, Dict
from ..projects import ProjectType

MetadataContents = Dict


class ProjectMetadata(Protocol):
    """
    An abstract interface for all metadata files.
    """

    def __file__(self) -> Optional[str]:
        """
        Return the metadata file, if one exists. Otherwise, return None.
        """

    def __name__(self) -> str:
        """
        Return the name of the project.
        """

    def __version__(self) -> str:
        """
        Return the project version.
        """

    def __type__(self) -> ProjectType:
        """
        Return the type of the project: package, application, or environment.
        If no type is specified in the metadata file, the "Package" type should be returned.
        """

    def __dependencies__(self) -> Set[Requirement]:
        """
        Return all required dependencies. For a standard metadata (pyproject.toml) file,
        this is the contents of the [project.dependencies] key.
        """

    def __optional__(self) -> Dict[str, Set[Requirement]]:
        """
        Return all optional dependencies. For a standard metadata (pyproject.toml) file,
        this is the contents of the [project.dependencies] key.
        """

    def __registries__(self) -> Optional[Dict[Requirement, str]]:
        """
        Return a dictionary which maps dependencies (both optional and required) to the
        registry URL from which they should be installed. Dependencies do not have to
        be mapped here! Any requirements not included in map should be installed from the
        public PyPI registry at pypi.org.
        """


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
