"""
A commandline-interface for the dimples package manager.
"""

from typing import Optional
from typer import Typer  # type: ignore

cli = Typer(no_args_is_help=True)


@cli.command()
def add(package: str, registry: Optional[str] = None):
    """Add the package to the current environment.

    If no [magenta]server[/] is provided, all known registries will be searched.
    """


@cli.command()
def remove(package: str):
    """Remove the package from the current environment."""


@cli.command()
def status(environment: Optional[str] = None):
    """Print's the environment status, including installed packages.

    If no [magenta]environment[/] is provided, the currently active environment is used.
    """


if __name__ == "__main__":
    from sys import exit

    exit(cli())
