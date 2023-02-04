"""
Package server implementations for the PyPI interface.
"""

import os
import sys
import typing
import dataclasses
import pypi_simple


@dataclasses.dataclass
class PyPIServer:
    """
    An implementation for all (simple API) PyPI package servers.
    """

    url: str = dataclasses.field(default=pypi_simple.PYPI_SIMPLE_ENDPOINT)
    trusted: typing.Optional[str] = dataclasses.field(
        default=None, kw_only=True, repr=False, hash=False
    )
    certificate: typing.Optional[str] = dataclasses.field(
        default=None, kw_only=True, repr=False, hash=False
    )
    authorization: typing.Optional[typing.Tuple[str, str]] = dataclasses.field(
        default=None, kw_only=True, repr=False, hash=False
    )

    def __distribution__(
        self, package: str, /, *, version: typing.Optional[str] = None
    ) -> str:
        """
        Returns the URL associated with the requested package distribution.
        """
        from .simple import distribution

        dist = distribution(
            package, version=version, url=self.url, auth=self.authorization
        )
        return dist.url

    def __packages__(self) -> set[str]:
        """
        Return the full set of all packages available on the PyPI server.
        """
        from .simple import index

        return {
            project
            for project in index(
                self.url,
                auth=self.authorization,
                certificate=self.certificate,
                trusted=self.trusted,
            ).projects
        }

    def __versions__(self, package: str) -> set[str]:
        """
        Return the set of all versions for the provided package.
        """
        from .simple import versions

        return versions(package, url=self.url, auth=self.authorization)

    def __download__(
        self,
        package: str,
        /,
        *,
        location: str = os.path.curdir,
        version: typing.Optional[str] = None,
    ) -> None:
        """
        Download the distribution for the specified package, and typing.Optionally specified
        version, to some location. If no version is provided, the largest version number
        found on the server should be used.
        """
        from .simple import download

        return download(
            package,
            version=version,
            location=location,
            url=self.url,
            auth=self.authorization,
        )


del pypi_simple, typing, dataclasses, sys, os
