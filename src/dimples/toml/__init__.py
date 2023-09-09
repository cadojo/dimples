"""
TOML readers and writers.
"""

import importlib.metadata

try:
    from tomllib import load, loads
except importlib.metadata.PackageNotFoundError:
    from tomli import load, loads

from tomli_w import dump, dumps

del importlib
