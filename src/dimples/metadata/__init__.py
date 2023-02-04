"""
Specifications, and parsers for Python project metadata files (pyproject.toml), and 
manifest files (pyproject.lock).
"""

import typing
import dataclasses
from ..packages import Package
from ..projects import ProjectType
from ..protocols.metadata import MetadataContents

from typing import Optional, Set, Dict, Iterable
from packaging.requirements import Requirement


@dataclasses.dataclass
class Metadata:
    """
    A simple type to abstract a project's metadata contained within pyproject.toml. Provides
    a __post_init__ method which validates the provided file.
    """

    file: str = dataclasses.field(hash=True)
    data: MetadataContents = dataclasses.field(hash=False)

    @property
    def dependencies(self) -> typing.Set[Requirement]:
        """
        Return the contents of the [project.dependencies] key.
        """
        from packaging.requirements import Requirement

        return {
            Requirement(dependency)
            for dependency in self.data["project"]["dependencies"]
        }

    @property
    def extras(self) -> typing.Dict[str, typing.Set[Requirement]]:
        """
        Return the contents of the [project.optional-dependencies] key, if it exists.
        Otherwise, return an empty dictionary.
        """
        from packaging.requirements import Requirement
        from typing import Dict, Set, cast

        deps = cast(
            Dict[str, Set[str]], self.data["project"].get("optional-dependencies", {})
        )

        return {
            extra: {Requirement(dependency) for dependency in dependencies}
            for (extra, dependencies) in deps.items()
        }

    @classmethod
    def default(
        cls,
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

    @classmethod
    def read(cls, file: str, /):
        """
        Load the contents of a metadata file.
        """
        from tomli import load
        from typing import cast
        from pathlib import Path
        from ..protocols.metadata import MetadataContents

        with open(str(Path(file).expanduser().resolve()), "rb") as stream:
            contents = cast(
                MetadataContents,
                load(stream),
            )

        return cls(file, contents)

    def __file__(self) -> typing.Optional[str]:
        """
        Return the manifest file, if one exists. Otherwise, return None.
        """
        return self.file

    def __type__(self) -> ProjectType:
        """
        Return the type of the project defined by the metadata file.
        """
        from typing import cast
        from ..projects import ProjectType

        data = self.data["tool"]["dimples"]["project"]
        return ProjectType(cast(str, data["type"]).capitalize())

    def __version__(self) -> str:
        """
        Return the version for the project.
        """
        from typing import List, cast

        try:
            return cast(str, self.data["project"]["version"])
        except KeyError:
            project = self.data["project"]
            try:
                if "version" in cast(List[str], project["dynamic"]):
                    raise NotImplementedError()
                else:
                    raise ValueError("Invalid metadata state!")
            except KeyError:
                raise ValueError("Invalid metadata state!")

    def __name__(self) -> str:
        """
        Return the name of the project.
        """
        from typing import cast

        return cast(str, self.data["project"]["name"])

    def __dependencies__(self) -> Set[Requirement]:
        """
        Return all required dependencies. For a standard metadata (pyproject.toml) file,
        this is the contents of the [project.dependencies] key.
        """
        return self.dependencies

    def __optional__(self) -> Dict[str, Set[Requirement]]:
        """
        Return all optional dependencies. For a standard metadata (pyproject.toml) file,
        this is the contents of the [project.dependencies] key.
        """
        return self.extras

    def __registries__(self) -> Optional[Dict[Requirement, str]]:
        """
        Return a dictionary which maps dependencies (both optional and required) to the
        registry URL from which they should be installed. Dependencies do not have to
        be mapped here! Any requirements not included in map should be installed from the
        public PyPI registry at pypi.org.
        """

    def __repr__(self):
        """
        Return a string representation of the Metadata instance.
        """
        return f"Metadata contents at {self.file}"


del dataclasses, typing, Package, ProjectType
