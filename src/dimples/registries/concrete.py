"""
Definitions and methods for registries.
"""

import dataclasses, typing


@dataclasses.dataclass(kw_only=True)
class Registry:
    """
    An implementation for a Python package registry.
    """

    url: str = dataclasses.field()
    alias: str = dataclasses.field()
    private: bool = dataclasses.field()

    def __alias__(self) -> str:
        """
        Return the alias of the registry.
        """
        return self.alias

    def __url__(self) -> str:
        """
        Return the URL of the registry.
        """
        return self.url

    def __private__(self) -> bool:
        """
        Returns False if the registry is publicly accessible.
        """
        return self.private


del dataclasses, typing
