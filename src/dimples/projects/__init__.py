"""
In this context, a project is a Python environment that may be associated with a 
Python package, or a Python workspace. 
"""

from __future__ import annotations

import enum
import typing

METADATA_FILE: typing.Literal["pyproject.toml"] = "pyproject.toml"
MANIFEST_FILE: typing.Literal["pyproject.lock"] = "pyproject.lock"

from dimples.projects import protocols


class Project:
    ...


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


del annotations, enum, typing
