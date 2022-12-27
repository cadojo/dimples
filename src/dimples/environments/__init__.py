"""
Interact with Python environments.
"""

import dataclasses, typing
from .manifests.protocols import ProjectManifest
from .metadata.protocols import ProjectMetadata
from ..registries.protocols import PythonRegistry

from .metadata import Metadata
from .manifests import Manifest


@dataclasses.dataclass
class Environment:
    """
    An implementation of the PythonEnvironment interface.
    """

    path: str = dataclasses.field()
    metadata: Metadata = dataclasses.field()
    manifest: Manifest = dataclasses.field()

    def __init__(self, path: str, /):
        from os.path import join
        from .. import METADATA_FILE, MANIFEST_FILE
        from .metadata import Metadata
        from .manifests import Manifest

        self.path = path
        self.metadata = Metadata(join(path, METADATA_FILE))
        self.manifest = Manifest(join(path, MANIFEST_FILE))

    def __environment__(self) -> str:
        """
        Returns the base path associated with the environment. There must be at least a
        metadata file (pyproject.toml) at this path. A manifest file will be created at this
        path, if the "dimples" package manager is used.
        """
        return self.path

    def __update__(self, *packages: str, cautious: bool = False, **kwargs) -> None:
        """
        Update every package in the environment. If cautious is set to False, an "eager"
        update style is applied, and every package dependency is also checked for
        update-ability.
        """
        raise NotImplementedError()

    def __metadata__(self) -> ProjectMetadata:
        """
        Return the set of explicitly installed Python packages.
        """
        return self.metadata

    def __manifest__(self) -> ProjectManifest:
        """
        Return the set of all installed Python packages (explicitly, or implicitly).
        """
        return self.manifest
