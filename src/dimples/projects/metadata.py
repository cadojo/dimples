"""
Types for interacting with `pyproject.toml` files.
"""

from __future__ import annotations

__export__ = {
    "ReadmeTable",
    "LicenseTable",
    "AuthorTable",
    "ProjectDict",
    "Table",
    "MetadataDict",
}

from typing_extensions import TypedDict, NotRequired
from typing import List, Union, Dict, Type


class ReadmeTable(TypedDict):
    """
    A typed dictionary for static type-checking the `[project.readme]` field of `pyproject.toml`.
    """

    file: str
    content_type: str


class LicenseTable(TypedDict):
    """
    A typed dictionary for static type-checking the `[project.license]` field of `pyproject.toml`.
    """

    file: NotRequired[str]
    text: NotRequired[str]


class AuthorTable(TypedDict):
    """
    A typed dictionary for static type-checking the `[project.authors]` and [project.maintainers] fields of `pyproject.toml`.
    """

    name: NotRequired[str]
    email: NotRequired[str]


class ProjectTable(TypedDict):
    """
    A typed dictionary for static type-checking the `[project]` fields of `pyproject.toml`.
    """

    authors: NotRequired[List[AuthorTable]]
    classifiers: NotRequired[List[str]]
    dependencies: NotRequired[List[str]]
    description: NotRequired[str]
    dynamic: NotRequired[List[str]]
    entry_points: NotRequired[Dict[str, str]]
    gui_scripts: NotRequired[Dict[str, str]]
    keywords: NotRequired[List[str]]
    license: NotRequired[LicenseTable]
    maintainers: NotRequired[List[AuthorTable]]
    name: str
    optional_dependencies: NotRequired[Dict[str, List[str]]]
    readme: NotRequired[Union[str, ReadmeTable]]
    requires_python: NotRequired[str]
    scripts: NotRequired[Dict[str, str]]
    urls: NotRequired[Dict[str, str]]
    version: NotRequired[str]


Table = Union[str, int, List, Dict[str, Union[str, int, Dict]]]


class MetadataDict(TypedDict):
    """
    A typed dictionary for static type-checking `pyproject.toml` file parsers.
    """

    project: ProjectTable
    tool: NotRequired[Table]


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
