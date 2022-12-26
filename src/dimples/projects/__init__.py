"""
Types relating to Python projects.
"""

from enum import Enum, auto


class ProjectType(Enum):
    """
    An enumerated type which captures all project types.
    """

    package = auto()
    application = auto()
    environment = auto()

    @classmethod
    def from_str(cls, label: str, /):
        """
        Given a string, return the appropriate project type.
        """
        return {
            "package": cls.package,
            "application": cls.application,
            "environment": cls.environment,
        }[label.lower()]


del Enum, auto
