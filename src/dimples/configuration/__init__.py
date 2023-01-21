"""
Global configuration options, and interfaces for parsing them.
"""

import dataclasses, typing
from ..registries.abstract import PythonRegistry


def registries() -> typing.Set[PythonRegistry]:
    """
    Parse the global registries file and return all configured registries.
    """
    from .. import GLOBAL_CONFIG, REGISTRY_FILE
    from ..toml import load
    from ..registries.concrete import Registry
    from pathlib import Path

    with open(str(Path(GLOBAL_CONFIG) / REGISTRY_FILE), "rb") as stream:
        data = load(stream)

    return {Registry(**registry) for registry in data.get("registries", set())}


def registry(*, alias: str = "", index: str = "") -> PythonRegistry:
    """
    Given a registry UUID, URL, or alias (in that order or preference), return the
    associated configured registry. Otherwise, raise a ValueError.
    """
    if index:
        key = index
        type = "index"
    elif alias:
        key = alias
        type = "alias"
    else:
        raise ValueError(
            "All keyword arguments are empty! Please specify a UUID, URL, or alias."
        )

    for registry in registries():
        if index and index == registry.__index__():
            return registry
        elif alias and alias == registry.__alias__():
            return registry

    raise ValueError(f"Registry with {type} '{key}' not found!")


del dataclasses, typing, PythonRegistry
