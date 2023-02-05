"""
Specifications, and parsers for Python project metadata files (pyproject.toml), and 
manifest files (pyproject.lock).
"""

__export__ = {
    "Metadata",
    "factories",
}

from typing import Iterable, Mapping, Optional, Set
from dataclasses import dataclass, field
from ..projects import ProjectType
from ..protocols.metadata import MetadataContents

from typing import Optional, Set, Dict
from packaging.requirements import Requirement


@dataclass
class CoreMetadata:
    """
    Represents Python package core metadata, with some improved (if I do say so)
    usability over Python-native packaging.metadata.metadata.
    """

    name: str = field()
    version: str = field()
    metadata_version: str = field()

    description: Optional[str] = field(kw_only=True, default=None)
    readme: Optional[str] = field(kw_only=True, default=None)
    requires_python: Optional[str] = field(kw_only=True, default=None)
    license: Optional[str] = field(kw_only=True, default=None)
    keywords: Optional[Iterable[str]] = field(kw_only=True, default=None)
    authors: Optional[Iterable[Mapping[str, str]]] = field(kw_only=True, default=None)


@dataclass
class Metadata:
    """
    A simple type to abstract a project's metadata contained within pyproject.toml.
    """

    file: str = field(hash=True)
    name: str = field(hash=True)

    contents: MetadataContents = field(hash=False)

    def dependencies(self) -> Set[Requirement]:
        """
        Return the contents of the [project.dependencies] key.
        """
        from packaging.requirements import Requirement

        return {
            Requirement(dependency)
            for dependency in self.contents["project"]["dependencies"]
        }

    def extras(self) -> Dict[str, Set[Requirement]]:
        """
        Return the contents of the [project.optional-dependencies] key, if it exists.
        Otherwise, return an empty dictionary.
        """
        from packaging.requirements import Requirement
        from typing import Dict, Set, cast

        deps = cast(
            Dict[str, Set[str]],
            self.contents["project"].get("optional-dependencies", {}),
        )

        return {
            extra: {Requirement(dependency) for dependency in dependencies}
            for (extra, dependencies) in deps.items()
        }

    @classmethod
    def read(cls, file: str, /):
        """
        Construct a Metadata instance from the provided contents.
        """
        from typing import cast
        from ..files import read, resolve
        from ..protocols.metadata import MetadataContents

        return cls(resolve(file), cast(MetadataContents, read(file)))

    def write(self, /):
        """
        Write the Metadata contents to the appropriate file.
        """
        from ..files import write

        return write(
            self.contents,
            self.file,
        )

    def __file__(self) -> Optional[str]:
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

        data = self.contents["tool"]["dimples"]["project"]
        return ProjectType(cast(str, data["type"]).capitalize())

    def __version__(self) -> str:
        """
        Return the version for the project.
        """
        from typing import List, cast

        try:
            return cast(str, self.contents["project"]["version"])
        except KeyError:
            project = self.contents["project"]
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

        return cast(str, self.contents["project"]["name"])

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


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
