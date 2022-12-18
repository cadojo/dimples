"""
Provides the capability to load pyproject.toml, and pyproject.lock files.
"""

__export__ = {"parse_metadata", "parse_manifest", "MetadataParser", "ManifestParser"}

from dataclasses import dataclass, field


def parse_metadata(path: str, /, validate: bool = True) -> dict:
    """
    Load the provided pyproject.toml file as a dictionary. If validate is set to True,
    fields relevant to "dimples" will be checked; if the fields are not valid, a ValueError
    is raised.
    """
    from pathlib import Path
    from warnings import warn
    from .toml import load
    from .. import METADATA_FILE

    with open(path, "rb") as file:
        metadata = load(file)

    if validate:
        if not path.endswith(METADATA_FILE):
            warn(f"The provided metadata file is not named {METADATA_FILE}!")

        try:
            metadata["project"]
            metadata["project"]["name"]
            metadata["project"]["dependencies"]
            metadata["tool"]["dimples"]["project"]["type"]
        except KeyError as error:
            raise ValueError("The provided metadata file is invalid.") from error

    return metadata


def parse_manifest(path: str, /, validate: bool = True) -> dict:
    """
    Load the provided pyproject.lock file as a dictionary. If validate is set to True,
    fields relevant to "dimples" will be checked; if the fields are not valid, a ValueError
    is raised.
    """
    from warnings import warn
    from .toml import load
    from .. import MANIFEST_FILE

    with open(path, "rb") as file:
        manifest = load(file)

    if validate:
        if not path.endswith(MANIFEST_FILE):
            warn(f"The provided manifest file is not named {MANIFEST_FILE}!")

        try:
            manifest["python"]["version"]
            manifest["manifest"]["version"]
            manifest["dependencies"]
            for dependency in manifest["dependencies"]:
                dependency["version"]
                dependency["index"]
                dependency["hash"]

        except KeyError as error:
            raise ValueError("The provided manifest file is invalid.") from error

    return manifest


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
