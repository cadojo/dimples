"""
Interfaces and implementations for Python package types.
"""

from typing import Set
from dataclasses import dataclass, field
from ..protocols.packages import PythonPackage


@dataclass(kw_only=True)
class Package:
    """
    A representation for a Python package.
    """

    name: str = field(kw_only=False)
    version: str = field(default="")
    dependencies: Set["Package"] = field(default_factory=set)
    registry: str = field(default="pypi")

    def __name__(self):
        """
        Return the package name.
        """
        return self.name

    def __version__(self):
        """
        Return the package version.
        """
        return self.version

    def __registry__(self):
        """
        Return the registry from which this package should be installed.
        """
        return self.registry

    def __dependencies__(self):
        """
        Return each explicitly defined dependency.
        """
        return self.dependencies


def name(package: PythonPackage, /):
    """
    Return the install-able name of the provided package.
    """
    return package.__name__()


def version(package: PythonPackage, /):
    """
    Return the installed version of the provided package. This is a simple wrapper around
    the importlib.metadata.version function!
    """
    return package.__version__()


def installed(package: PythonPackage, /):
    """
    Returns True if the package is installed, and False otherwise.
    """
    from importlib.metadata import PackageNotFoundError

    try:
        version(package)
    except PackageNotFoundError:
        return False

    return True


def registry(package: PythonPackage, /):
    """
    Return the registry from which the provided package was installed.
    """
    return package.__registry__()


def dependencies(package: PythonPackage, /):
    """
    Return each explicitly defined dependency.
    """
    return package.__dependencies__()


del dataclass, field, Set, PythonPackage
