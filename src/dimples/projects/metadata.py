"""
Types for interacting with `pyproject.toml` files.
"""

from __future__ import annotations


__export__ = {
    "content",
    "project",
    "tool",
}

import pyproject_parser
import pathlib
from dimples.projects.protocols import DimplesDict, ProjectDict


def content(filepath: str | pathlib.Path, /) -> pyproject_parser.PyProject:
    """
    Return the full contents of the provided pyproject.toml file.
    """
    from pyproject_parser import PyProject
    from pathlib import Path

    return PyProject.load(str(Path(filepath).resolve()))


def project(filepath: str | pathlib.Path, /) -> ProjectDict:
    """
    Return the contents of the [project] key in the provided pyproject.toml file.
    """
    from dimples.toml import load
    from pathlib import Path
    from typing import cast
    from dimples.projects.protocols import ProjectDict

    with open(str(Path(filepath).resolve()), "rb") as io:
        content = load(io)

    return cast(ProjectDict, content["project"])


def tool(filepath: str | pathlib.Path, /) -> DimplesDict:
    """
    Return the contents of the [tool.dimples] key in the provided pyproject.toml file.
    """
    from dimples.toml import load
    from pathlib import Path
    from typing import cast
    from dimples.projects.protocols import DimplesDict, ProjectDict

    with open(str(Path(filepath).resolve()), "rb") as io:
        content = load(io)

    try:
        return cast(DimplesDict, content["tool"]["dimples"])
    except KeyError:
        return {"uuid": None}


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
