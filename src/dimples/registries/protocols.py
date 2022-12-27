"""
Abstract interfaces for Python package registries.
"""


__export__ = {
    "PythonRegistry",
}

from typing import Protocol, Optional


class PythonRegistry(Protocol):
    """
    An abstract interface for Python registries.
    """

    def __alias__(self) -> str:
        """
        Return the alias of the registry.
        """

    def __url__(self) -> str:
        """
        Return the URL of the registry.
        """

    def __private__(self) -> bool:
        """
        Returns False if the registry is publicly accessible.
        """

    def __uuid__(self) -> Optional[str]:
        """
        Return the UUID associated with the registry, if one exists. Otherwise, return None.
        """

    def __update__(self) -> None:
        """
        Fetch the latest package metadata changes from the registry.
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
