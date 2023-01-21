"""
Load tomli for Python versions less than 3.10. Otherwise, load tomllib!
"""

try:
    from tomllib import load, loads  # type: ignore
except ModuleNotFoundError:
    from tomli import load, loads  # type: ignore
