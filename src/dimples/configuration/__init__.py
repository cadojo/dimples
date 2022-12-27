"""
Global configuration options, and interfaces for parsing them.
"""

import dataclasses, typing
from ..registries.protocols import PythonRegistry


def registries() -> typing.Set[PythonRegistry]:
    """
    Parse the global registries file and return all configured registries.
    """
    from .. import GLOBAL_CONFIG, REGISTRY_FILE
    from ..toml import load
    from ..registries import Registry
    from pathlib import Path
    from typing import Set
    from ..registries.protocols import PythonRegistry

    with open(str(Path(GLOBAL_CONFIG) / REGISTRY_FILE), "rb") as stream:
        data = load(stream)

    registries: Set[PythonRegistry] = {
        Registry(**reg) for reg in data.get("registries", set())
    }

    return registries


def registry(*, alias: str = "", url: str = "", uuid: str = "") -> PythonRegistry:
    """
    Given a registry UUID, URL, or alias (in that order or preference), return the
    associated configured registry. Otherwise, raise a ValueError.
    """
    if uuid:
        key = uuid
        type = "uuid"
    elif url:
        key = url
        type = "url"
    elif alias:
        key = alias
        type = "alias"
    else:
        raise ValueError(
            "All keyword arguments are empty! Please specify a UUID, URL, or alias."
        )

    for registry in registries():
        if uuid and uuid == registry.__uuid__():
            return registry
        elif url and url == registry.__url__():
            return registry
        elif alias and alias == registry.__alias__():
            return registry

    raise ValueError(f"Registry with {type} '{key}' not found!")


del dataclasses, typing, PythonRegistry
