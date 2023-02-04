"""
Types relating to Python projects.
"""

from __future__ import annotations as __annotations
from enum import Enum, auto


class ProjectType(Enum):
    """
    An enumerated type which captures all project types.
    """

    Package = "Package"
    Application = "Application"
    Environment = "Environment"

    @classmethod
    def from_str(cls, label: str, /) -> ProjectType:
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
        return self.value

    def __repr__(self):
        """
        Return a string representation of the enumerated type.
        """
        return f"ProjectType: {self}"


del Enum, auto
