"""
Abstract interfaces for environment metadata files.
"""

__export__ = {
    "ProjectMetadata",
}

from typing import Protocol, Optional, Dict
from ...projects import ProjectType


class ProjectMetadata(Protocol):
    """
    An abstract interface for all metadata files.
    """

    def __file__(self) -> Optional[str]:
        """
        Return the manifest file, if one exists. Otherwise, return None.
        """

    def __project__(self) -> Dict[str, str]:
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
