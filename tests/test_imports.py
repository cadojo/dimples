"""
Can 'dimp', and all of its subpackages and modules, be imported without error?
"""


def test_import():
    """
    Can every module be imported without error?
    """
    import dimples.packages
    import dimples.registries
    import dimples.configuration.constants
    import dimples.metadata
    import dimples.manifests
    import dimples.projects
    import dimples.toml
    import dimples.environments.sites
    import dimples.managers
    import dimples.servers.pypi.simple

    import dimples.protocols.packages
    import dimples.protocols.registries
    import dimples.protocols.metadata
    import dimples.protocols.manifests
    import dimples.protocols.environments
    import dimples.protocols.configuration
    import dimples.protocols.servers
