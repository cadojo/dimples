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
    private: bool = dataclasses.field(default=False)
    uuid: typing.Optional[str] = dataclasses.field(default=None)

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

    def __uuid__(self) -> typing.Optional[str]:
        """
        Return the UUID associated with the registry, if one exists. Otherwise, return None.
        """
        return self.uuid

    def __update__(self) -> None:
        """
        Fetch the latest package metadata changes from the registry.
        """
        raise NotImplementedError()


del dataclasses, typing
