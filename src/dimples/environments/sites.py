"""
Functions for finding install-locations.
"""


def user():
    """
    Returns the directory where packages are installed for the active user.
    """
    import site

    return site.getusersitepackages()


def environment():
    """
    Returns the directory where packages are installed for the active environment.
    Beware! This does not work in an IPython session.
    """
    import sysconfig

    try:
        return sysconfig.get_paths()["purelib"]
    except KeyError:
        return sysconfig.get_path("purelib")
