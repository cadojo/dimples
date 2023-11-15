"""
Interfaces for Python projects, without any implementations.
"""

__export__ = {
    "DimplesDict",
    "ProjectDict",
}


import typing
import uuid
import pyproject_parser


ProjectDict = pyproject_parser.ProjectDict  # type: ignore


class ManifestConfigurationDict(typing.TypedDict):
    """
    Types for the pyproject.lock [configuration] key.
    """

    python_version: str
    manifest_version: str
    project_hash: str


class ManifestDependencyDict(typing.TypedDict):
    """
    Types for values of the pyproject.lock [dependencies] key.
    """

    version: str
    uuid: typing.NotRequired[str]


class ManifestDict(typing.TypedDict):
    """
    Types for the pyproject.lock file.
    """

    configuration: ManifestConfigurationDict
    dependencies: typing.Dict[str, ManifestDependencyDict]


class DimplesDict(typing.TypedDict):
    """
    Types for the pyproject.toml [tool.dimples] key.
    """

    uuid: typing.NotRequired[str]
    dependencies: typing.NotRequired[typing.Dict[str, str]]


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
