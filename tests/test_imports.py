"""
Can 'dimp', and all of its subpackages and modules, be imported without error?
"""


def test_import():
    import dimples
    import dimples.servers
    import dimples.registries
    import dimples.packages
    import dimples.environments
