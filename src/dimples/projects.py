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
            "Package": cls.Package,
            "Application": cls.Application,
            "Environment": cls.Environment,
        }[label.capitalize()]

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return {
            self.Package.value: "Package",
            self.Application.value: "Application",
            self.Environment.value: "Environment",
        }[self.value]

    def __repr__(self):
        """
        Return a string representation of the enumerated type.
        """
        return f"ProjectType: {self}"


del Enum, auto
