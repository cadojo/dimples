"""
Provides the capability to load pyproject.toml, and pyproject.lock files.
"""

__export__ = {
    "metadata",
    "manifest",
}


from typing import Any, Dict


def metadata(data: Dict[str, Any], /) -> bool:
    """
    Load the provided pyproject.toml file as a dictionary. If validate is set to True,
    fields relevant to "dimples" will be checked; if the fields are not valid, a ValueError
    is raised.
    """

    try:
        data["project"]
        data["project"]["name"]
        data["project"]["dependencies"]
        data["tool"]["dimples"]["project"]["type"]
    except KeyError:
        return False

    return True


def manifest(data: Dict[str, Any], /) -> bool:
    """
    Load the provided pyproject.toml file as a dictionary. If validate is set to True,
    fields relevant to "dimples" will be checked; if the fields are not valid, a ValueError
    is raised.
    """

    try:
        data["metadata"]
        data["metadata"]["python"]
        data["metadata"]["version"]
        data["manifest"]
        data["manifest"]["dependencies"]

        for dependency in data["manifest"]["dependencies"]:
            dependency["version"]
            dependency["index"]
            dependency["hash"]
            dependency["dependencies"]

    except KeyError:
        return False

    return True


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
