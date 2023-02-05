"""
Types relating to Python projects.
"""

__export__ = {
    "ProjectType",
}

from enum import Enum


class ProjectType(Enum):
    """
    An enumerated type which captures all project types.
    """

    Package = "Package"
    Application = "Application"
    Workspace = "Workspace"

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return self.value

    def __repr__(self):
        """
        Return a string representation of the enumerated type.
        """
        return f"ProjectType: {str(self)}"


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
