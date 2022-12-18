"""
Can 'dimp', and all of its subpackages and modules, be imported without error?
"""


def test_import():
    import dimples.servers.protocols
    import dimples.servers.pypi.simple
    import dimples.registries.protocols
    import dimples.packages.protocols
    import dimples.environments.protocols
    import dimples.environments.parsers
    import dimples.environments.sites
