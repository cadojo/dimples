"""
A modern Python package manager which supports _registries_ in addition to indexes!

A Python _registry_ is different than a Python _index_. All indexes (indices?) are treated 
as the same! A package's name is considered to be a unique identifier. This was set up so 
the public Python index, PyPi, could have mirrors all over the world without issue. 

But the web has grown since PyPi was founded! No one uses mirrors; everyone installs public
packages from PyPi, and some install private packages from privately hosted indexes.

Modern languages use registries. A package's name should be unique on a given _registry_, 
but other packages with the name may exist on _other_ registries. A UUID is used to uniquely
identify each package. This is cryptographically guaranteed.

The odds are _way_ against this project, but I really think something like this should 
exist. Python package metadata can be pulled from PyPi servers pretty easily. The "only"
thing we need for registries to exist within Python is for...

  1. ...package metadata to contain UUIDs, and...
  2. ...package managers to store both either UUIDs --- or _registry URLs_ --- for each installed package.
  
Hey, that's only two things!
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("dimples")
except PackageNotFoundError:
    __version__ = "unknown"

del version, PackageNotFoundError

import typing


METADATA_FILE: typing.Literal["pyproject.toml"] = "pyproject.toml"
MANIFEST_FILE: typing.Literal["pyproject.lock"] = "pyproject.lock"
REGISTRY_FILE: typing.Literal["registries.toml"] = "registries.toml"
GLOBAL_CONFIG: typing.Literal["~/.python"] = "~/.python"

del typing
