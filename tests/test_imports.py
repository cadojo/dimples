"""
Can 'dimp', and all of its subpackages and modules, be imported without error?
"""


def test_import():
    """
    Can every module be imported without error?
    """
    import dimples.servers.protocols
    import dimples.servers.pypi.simple

    import dimples.registries.protocols

    import dimples.packages.protocols

    import dimples.environments.protocols
    import dimples.environments.formats.validate
    import dimples.environments.sites

    import dimples.managers.protocols
