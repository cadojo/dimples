"""
Interfaces for Python projects, without any implementations.
"""

__export__ = {
    "PythonProject",
    "DimplesDict",
    "ProjectDict",
}

import typing
import uuid

import pyproject_parser

ProjectDict = pyproject_parser.ProjectDict  # type: ignore


class DimplesDict(typing.TypedDict):
    """
    Types for the pyproject.toml [tool.dimples] key.
    """

    uuid: typing.Optional[str]


class PythonProject(typing.Protocol):
    """
    A standard interface for all Python project types: packages, and workspaces.
    """

    def __path__(self) -> str:
        """
        The path to the Python project directory or folder.
        """
        ...

    def __name__(self) -> typing.Optional[str]:
        """
        Return the name of the package.
        """
        ...

    def __uuid__(self) -> typing.Optional[uuid.UUID]:
        """
        Return a unique identifier that is tied to the package, if one is known.
        """
        ...


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
