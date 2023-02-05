"""
Read and write methods for the dimples configuration file type: TOML.
"""

__export__ = {
    "read",
    "write",
    "resolve",
}

from typing import Dict, Any


def resolve(file: str, /):
    """
    Resolve the filename, expanding all user characters and directory markings.
    """
    from pathlib import Path

    return str(Path(file).expanduser().absolute().resolve())


def read(file: str, /):
    """
    Load the contents of a metadata file.
    """
    from tomli import load

    with open(resolve(file), "rb") as stream:
        contents = load(stream)

    return contents


def write(contents: Dict[str, Any], file: str):
    """
    Write the metadata contents to the provided file.
    """

    from tomli_w import dump

    with open(resolve(file), "rb") as stream:
        dump(contents, stream)


if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
