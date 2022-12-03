"""
A modern Python package manager which supports _registries_ in addition to indexes!

A Python _registry_ is different than a Python _index_. All indexes (indices?) are treated 
as the same! A package's name is considered to be a unique identifier. This was set up so 
the public Python index, PyPi, could have mirrors all over the world without issue. 

But the web has grown since PyPi was founded! No one uses mirrors; everyone installs public
packages from PyPi, and some install private packages from privately hosted indexes.

Modern langaages use registries. A package's name should be unique on a given _registry_, 
but other packages with the name may exist on _other_ registries. A UUID is used to uniquely
identify each package. This is cryptographically guaranteed.

The odds are _way_ against this project, but I really think something like this should 
exist. Python package metadata can be pulled from PyPi servers pretty easily. The "only"
thing we need for registries to exist within Python is for...

  1. Package metadata to contain UUIDs
  2. Package managers to store both both UUIDs, and _registry URLs_ for each installed package
  
Hey, that's only two things!
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("crpm")
except PackageNotFoundError:
    __version__ = "unknown"

del version, PackageNotFoundError
