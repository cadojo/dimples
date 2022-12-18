"""
Abstract interfaces for Python package registries.
"""


__export__ = {
    "PythonRegistry",
}

from typing import Protocol


class PythonRegistry(Protocol):
    """
    An abstract interface for Python registries.
    """

    def __alias__(self) -> str:
        """
        Return the alias of the registry.
        """

    def __registry__(self) -> str:
        """
        Return the URL of the registry.
        """

    def __public__(self) -> bool:
        """
        Returns True if the registry is publicly accessible.
        """

    def __update__(self) -> None:
        """
        Fetch the latest package metadata changes from the registry.
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
