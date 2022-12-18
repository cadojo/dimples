"""
A REST api for interacting with PyPi servers.
"""

__export__ = {
    "index",
    "metadata",
    "versions",
    "distribution",
    "download",
    "PyPIServer",
}

from typing import Optional, NamedTuple, Tuple, Union
from pypi_simple import (
    PYPI_SIMPLE_ENDPOINT,
    DistributionPackage,
    ProjectPage,
    IndexPage,
)
from functools import cache
from os.path import curdir
from dataclasses import dataclass, field


@cache
def index(
    url: str = PYPI_SIMPLE_ENDPOINT,
    /,
    *,
    auth: Optional[Tuple[str, str]] = None,
    trusted: Union[str, bool, None] = None,
    certificate: Optional[str] = None,
) -> IndexPage:
    from requests import Session
    from pypi_simple import PyPISimple

    if trusted or certificate:
        session = Session()
        session.cert = certificate
        session.verify = trusted
        session.auth = auth

        with PyPISimple(endpoint=url, session=session) as client:
            data = client.get_index_page()
    else:
        with PyPISimple(endpoint=url, auth=auth) as client:
            data = client.get_index_page()

    return data


@cache
def metadata(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[Tuple[str, str]] = None,
    trusted: Union[str, bool, None] = None,
    certificate: Optional[str] = None,
) -> ProjectPage:
    """
    Fetch metadata for the provided package.
    """
    from requests import Session
    from pypi_simple import PyPISimple

    if trusted or certificate:
        session = Session()
        session.cert = certificate
        session.verify = trusted
        session.auth = auth

        with PyPISimple(endpoint=url, session=session) as client:
            data = client.get_project_page(package)
    else:
        with PyPISimple(endpoint=url, auth=auth) as client:
            data = client.get_project_page(package)

    return data


@cache
def versions(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[Tuple[str, str]] = None,
) -> set[str]:
    """
    Fetch all available versions of the provided package.
    """
    data = metadata(package, url=url, auth=auth)
    return {
        distribution.version
        for distribution in data.packages
        if distribution.version is not None
    }


@cache
def distribution(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[Tuple[str, str]] = None,
    version: Optional[str] = None,
) -> DistributionPackage:
    """
    Returns a `pypi_simple.DistributionPackage` instance for the specified package, and
    optionally a specific version. If no version is specified, the latest version is used.
    """
    from packaging.version import parse, Version

    data = metadata(package, url=url, auth=auth)

    vs = [parse(p.version) for p in data.packages if p.version]

    if version:

        try:
            i = vs.index(parse(version))
        except ValueError:
            raise ValueError(f"The specified version, {version} was not found!")

        return data.packages[i]

    else:
        # The "if p.version" here is critical! It allows packages.sort to be type stable!
        packages = [p for p in data.packages if p.version]
        packages.sort(key=lambda p: parse(str(p.version)), reverse=True)
        return packages[0]


def download(
    package: str,
    /,
    *,
    url: str = PYPI_SIMPLE_ENDPOINT,
    auth: Optional[Tuple[str, str]] = None,
    location: str = curdir,
    version: Optional[str] = None,
) -> None:
    """
    Download the requested package, and optionally requested version.

    The `to` keyword argument specifies the download location, and defaults to the current
    directory. The `version` keyword argument specifies the desired package version. If no
    version is specified, the highest version number is used.
    """
    from pathlib import Path
    from requests import get

    dist = distribution(package, url=url, auth=auth, version=version)

    response = get(dist.url)
    _location = Path(location) / dist.filename

    with open(_location, "wb") as file:
        file.write(response.content)


@dataclass
class PyPIServer:
    """
    An implementation for all (simple API) PyPI package servers.
    """

    __slots__ = (
        "url",
        "trusted",
        "authorization",
    )

    url: str = field(default=PYPI_SIMPLE_ENDPOINT)
    trusted: Optional[str] = field(default=None, kw_only=True, repr=False, hash=False)
    authorization: Optional[Tuple[str, str]] = field(
        default=None, kw_only=True, repr=False, hash=False
    )

    def __distribution__(
        self, package: str, /, *, version: Optional[str] = None
    ) -> str:
        """
        Returns the URL associated with the requested package distribution.
        """
        dist = distribution(
            package, version=version, url=self.url, auth=self.authorization
        )
        return dist.url

    def __versions__(self, package: str) -> set[str]:
        """
        Return the set of all versions for the provided package.
        """
        return versions(package, url=self.url, auth=self.authorization)

    def __download__(
        self, package: str, /, *, location: str = curdir, version: Optional[str] = None
    ) -> None:
        """
        Download the distribution for the specified package, and optionally specified
        version, to some location. If no version is provided, the largest version number
        found on the server should be used.
        """
        return download(
            package,
            version=version,
            location=location,
            url=self.url,
            auth=self.authorization,
        )


if __name__ == "__main__":
    ...
else:
    import hygiene  # type: ignore

    hygiene.cleanup()
