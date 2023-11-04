"""
Types for interacting with `pyproject.toml` files.
"""

from __future__ import annotations


__export__ = {
    "DimplesDict",
    "content",
    "project",
    "dimples",
}

import pyproject_parser
import pathlib
from typing import TypedDict, Optional


class DimplesDict(TypedDict):
    """
    Types for the pyproject.toml [tool.dimples] key.
    """

    uuid: Optional[str]


def content(filepath: str | pathlib.Path, /) -> pyproject_parser.PyProject:
    """
    Return the full contents of the provided pyproject.toml file.
    """
    from pyproject_parser import PyProject
    from pathlib import Path

    return PyProject.load(str(Path(filepath).resolve()))


def project(filepath: str | pathlib.Path, /) -> pyproject_parser.ProjectDict:
    """
    Return the contents of the [project] key in the provided pyproject.toml file.
    """
    from dimples.toml import load
    from pathlib import Path
    from typing import cast
    from pyproject_parser import ProjectDict

    with open(str(Path(filepath).resolve()), "rb") as io:
        content = load(io)

    return cast(ProjectDict, content["project"])


def dimples(filepath: str | pathlib.Path, /) -> DimplesDict:
    """
    Return the contents of the [tool.dimples] key in the provided pyproject.toml file.
    """
    from dimples.toml import load
    from pathlib import Path
    from typing import cast
    from pyproject_parser import ProjectDict

    with open(str(Path(filepath).resolve()), "rb") as io:
        content = load(io)

    return content["tool"].get("dimples", {"uuid": None})


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
