"""
Wrappers around the pypi-simple package for interacting with PyPI's Simple API.
"""

__export__ = {
    "index",
    "metadata",
    "versions",
    "distribution",
    "download",
}

from os.path import curdir
from typing import Optional, Tuple, Union
from pypi_simple import (
    PYPI_SIMPLE_ENDPOINT,
    DistributionPackage,
    ProjectPage,
    IndexPage,
)


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
    from packaging.version import parse

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
        return next(iter(packages))


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


if __name__ == "__main__":
    ...
else:
    import hygiene

    hygiene.cleanup()
