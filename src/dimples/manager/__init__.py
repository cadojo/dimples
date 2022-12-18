"""
Interfaces and implementations for a user-facing package manager.
"""

__export__ = {
    "PackageManager",
}

from typing import Protocol


class PackageManager(Protocol):
    """
    An abstract interface for all user-facing Python package managers.
    """
