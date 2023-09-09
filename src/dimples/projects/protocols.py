"""
Interfaces for Python projects, without any implementations.
"""

import typing
import uuid


class PythonProject(typing.Protocol):
    """
    A standard interface for all Python project types: packages, and workspaces.
    """

    def __path__(self) -> str:
        """
        The path to the Python project directory or folder.
        """
        ...


class PythonPackage(PythonProject, typing.Protocol):
    """
    A standard interface for all Python packages.
    """

    def __name__(self) -> str:
        """
        Return the name of the package.
        """
        ...

    def __uuid__(self) -> typing.Optional[uuid.UUID]:
        """
        Return a unique identifier that is tied to the package, if one is known.
        """
        ...


class PythonWorkspace(PythonProject, typing.Protocol):
    """
    A standard interface for all Python workspaces; environments that are not tied
    to one particular installable Python package.
    """


del typing, uuid
