"""
Load tomli for Python versions less than 3.10. Otherwise, load tomllib!
"""

try:
    from tomllib import *  # type: ignore
except ModuleNotFoundError:
    from tomli import *  # type: ignore
