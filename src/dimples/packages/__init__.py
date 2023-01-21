"""
Interfaces and implementations for Python package types.
"""

from . import abstract, concrete


def name(package: abstract.PythonPackage, /):
    """
    Return the install-able name of the provided package.
    """
    return package.__name__()


def version(package: abstract.PythonPackage, /):
    """
    Return the installed version of the provided package. This is a simple wrapper around
    the importlib.metadata.version function!
    """
    return package.__version__()


def installed(package: abstract.PythonPackage, /):
    """
    Returns True if the package is installed, and False otherwise.
    """
    from importlib.metadata import PackageNotFoundError

    try:
        version(package)
    except PackageNotFoundError:
        return False

    return True


def registry(package: abstract.PythonPackage, /):
    """
    Return the registry from which the provided package was installed.
    """
    return package.__registry__()


def dependencies(package: abstract.PythonPackage, /):
    """
    Return each explicitly defined dependency.
    """
    return package.__dependencies__()
