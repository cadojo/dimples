"""
Specifications, and parsers for Python project metadata files (pyproject.toml), and 
manifest files (pyproject.lock).
"""

import typing, dataclasses
from ..packages import Package
from ..projects import ProjectType
from ..protocols.metadata import MetadataContents

from typing import Optional, Set, Dict
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

    def __init__(self, file: str, /):
        """
        Load the provided metadata file.
        """
        from ..toml import load
        from typing import cast
        from pathlib import Path

        path = str(Path(file).expanduser().resolve())

        with open(path, "rb") as stream:
            data = load(stream)

        self.data: MetadataContents = cast(MetadataContents, data)
        self.file = path

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
        return ProjectType.from_str(cast(str, data["type"]))

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
