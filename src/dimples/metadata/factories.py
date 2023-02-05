"""
Constructors of metadata contents.
"""

__export__ = {
    "default",
}

from typing import Iterable
from ..projects import ProjectType


def default(
    name: str,
    *,
    version: str = "0.1.0",
    description: str = "",
    author: str = "",
    email: str = "",
    type: ProjectType = ProjectType.Package,
    typed: bool = True,
    python: str = "3.7",
    backend: str = "hatchling.build",
    license: str = "MIT",
    keywords: Iterable[str] = set(),
    cpython: bool = True,
    pypy: bool = True,
    script: str = "",
    strict: bool = False,
):
    """
    Return default metadata contents for a Python project.
    """
    from packaging.version import Version
    from collections import OrderedDict
    from typing import MutableMapping, Any, Union, List
    from ..protocols.metadata import MetadataContents

    build: MutableMapping[str, str] = OrderedDict()
    build["requires"] = backend.split(".")[0]
    build["build-backend"] = backend

    versions = (
        f"Programming Language :: Python :: {v}"
        for v in (f"3.{i}" for i in range(12))
        if Version(v) >= Version(python)
    )

    implementations = []

    if cpython:
        implementations.append(
            "Programming Language :: Python :: Implementation :: CPython"
        )
    if pypy:
        implementations.append(
            "Programming Language :: Python :: Implementation :: PyPy"
        )

    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        *versions,
        *implementations,
    ]

    dependencies: List[str] = []
    optional: MutableMapping[str, List[str]] = {}

    if typed:
        classifiers.append(
            "Typing :: Typed",
        )

    project: MutableMapping[
        str,
        Union[
            str,
            List[str],
            List[MutableMapping[str, str]],
            MutableMapping[str, str],
            MutableMapping[str, List[str]],
        ],
    ] = OrderedDict()
    project["name"] = name
    project["description"] = description
    project["readme"] = "README.md"
    project["requires-python"] = f">={python}"
    project["license"] = license
    project["version"] = version
    project["keywords"] = [*keywords]

    first: MutableMapping[str, str] = OrderedDict()
    first["name"] = author
    first["email"] = email
    project["authors"] = [
        first,
    ]

    project["classifiers"] = classifiers
    project["dependencies"] = dependencies
    project["optional-dependencies"] = optional

    if script:
        project["scripts"] = {script: f"{name}.__main__"}

    tools: OrderedDict[str, Any] = OrderedDict()

    if "hatchling" in backend:
        tools["hatch"] = OrderedDict()
        tools["hatch"]["build"] = OrderedDict()
        tools["hatch"]["build"]["packages"] = [f"src/{name}"]

        if typed:
            tools["hatch"]["build"]["include"] = ["py.typed"]

    tools["dimples"] = OrderedDict()
    tools["dimples"]["project"] = OrderedDict()
    tools["dimples"]["project"]["type"] = str(type)
    tools["dimples"]["project"]["strict"] = strict

    metadata: MetadataContents = OrderedDict()

    metadata["build-system"] = build
    metadata["project"] = project
    metadata["tool"] = tools

    return metadata


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
