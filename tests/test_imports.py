"""
Can 'dimp', and all of its subpackages and modules, be imported without error?
"""


def test_import():
    """
    Can every module be imported without error?
    """
    import dimples.servers.protocols
    import dimples.servers.pypi.simple

    import dimples.registries.abstract

    import dimples.packages.abstract

    import dimples.environments.abstract
    import dimples.environments.validate
    import dimples.environments.sites

    import dimples.environments.metadata.abstract
    import dimples.environments.manifests.abstract

    import dimples.managers.abstract
