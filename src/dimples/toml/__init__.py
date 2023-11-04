"""
TOML readers and writers.
"""

__export__ = {
    "load",
    "loads",
    "dump",
    "dumps",
}

import importlib.metadata

try:
    from tomllib import load, loads  # type: ignore
except importlib.metadata.PackageNotFoundError:
    from tomli import load, loads  # type: ignore

from tomli_w import dump, dumps

if __name__ != "__main__":
    import hygiene

    hygiene.cleanup()
