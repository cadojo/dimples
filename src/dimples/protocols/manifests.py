"""
Abstract interfaces for environment manifest files.
"""

__export__ = {
    "ProjectManifest",
}

from typing import Protocol, Optional


class ProjectManifest(Protocol):
    """
    An abstract interface for all manifest files.
    """

    def __file__(self) -> Optional[str]:
        """
        Return the manifest file, if one exists. Otherwise, return None.
        """


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
