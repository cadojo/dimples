"""
Interfaces for global configuration options.
"""

__export__ = {
    "GlobalConfiguration",
}

from typing import Protocol, Set
from ..registries.abstract import PythonRegistry


class GlobalConfiguration(Protocol):
    """
    An abstract interface for all global configuration parsers.
    """

    def __registries__(self) -> Set[PythonRegistry]:
        """
        Parse the global registries file and return all configured registries.
        """

    def __registry__(
        self, *, alias: str = "", url: str = "", uuid: str = ""
    ) -> PythonRegistry:
        """
        Given a registry UUID, URL, or alias (in that order or preference), return the
        associated configured registry. Otherwise, raise a ValueError.
        """


if __name__ != "__main__":
    import hygiene  # type: ignore

    hygiene.cleanup()
