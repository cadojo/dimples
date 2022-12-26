"""
Definitions and methods for registries.
"""

import dataclasses, typing


@dataclasses.dataclass
class Registry:
    """
    An implementation for a Python package registry.
    """

    url: str = dataclasses.field()
    alias: str = dataclasses.field()
    public: bool = dataclasses.field()

    def __alias__(self) -> str:
        """
        Return the alias of the registry.
        """
        return self.alias

    def __registry__(self) -> str:
        """
        Return the URL of the registry.
        """
        return self.url

    def __public__(self) -> bool:
        """
        Returns True if the registry is publicly accessible.
        """
        return self.public

    def __update__(self) -> None:
        """
        Fetch the latest package metadata changes from the registry.
        """
        raise NotImplementedError()


del dataclasses, typing
