"""
In this context, a project is a Python environment that may be associated with a 
Python package, or a Python workspace. 
"""

from __future__ import annotations

import enum
import typing
import pyproject_metadata

METADATA_FILE: typing.Literal["pyproject.toml"] = "pyproject.toml"
MANIFEST_FILE: typing.Literal["pyproject.lock"] = "pyproject.lock"

from dimples.projects import protocols


class ProjectType(enum.Enum):
    """
    All of the different kinds of projects! A PACKAGE is any project that is tied
    to a standard Python package structure; these are projects you can install with
    `pip`, or `dmp`. A WORKSPACE is any project that is not tied to a standard Python
    package; these projects are collections of programs, possibly for some kind of
    collective analysis, that all use the same Python environment.
    """

    PACKAGE = enum.auto()
    WORKSPACE = enum.auto()


def path(project: protocols.PythonProject, /) -> str:
    """
    Return the full, resolved path to the project directory or folder.

    This uses the `pathlib` package to resolve the project's path.
    """
    from pathlib import Path

    return str(Path(project.__path__()).resolve())


def metadata_file(project: protocols.PythonProject, /) -> str:
    """
    Return the full, resolved path to the metadata file.

    This uses the `pathlib` package to resolve the project's path.
    """
    import os.path

    return os.path.join(
        path(project),
        METADATA_FILE,
    )


def manifest_file(project: protocols.PythonProject, /) -> str:
    """
    Return the full, resolved path to the manifest file.

    this uses the `pathlib` package to resolve the project's path.
    """
    import os.path

    return os.path.join(
        path(project),
        MANIFEST_FILE,
    )


def metadata(
    project: protocols.PythonProject, /
) -> pyproject_metadata.StandardMetadata:
    """
    Given any project, return the contents of `pyproject.toml`.
    """
    from dimples import toml
    from pyproject_metadata import StandardMetadata

    with open(metadata_file(project), "rb") as file:
        data = toml.load(file)

    return StandardMetadata.from_pyproject(data, path(project))


def requirements(
    project: protocols.PythonProject, /
) -> typing.Set[protocols.PythonProject]:
    """
    Return all package requirements.
    """
    # md = metadata(project)
    ...


del annotations, enum, typing, pyproject_metadata
