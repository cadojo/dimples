"""
Types relating to Python projects.
"""

from enum import Enum, auto


class ProjectType(Enum):
    """
    An enumerated type which captures all project types.
    """

    Package = auto()
    Application = auto()
    Environment = auto()

    @classmethod
    def from_str(cls, label: str, /):
        """
        Given a string, return the appropriate project type.
        """
        return {
            "package": cls.Package,
            "application": cls.Application,
            "environment": cls.Environment,
        }[label.lower()]

    def to_str(self):
        """
        Return a string representation of the object.
        """
        return {
            self.Package: "Package",
            self.Application: "Application",
            self.Environment: "Environment",
        }[self.value]


del Enum, auto
