"""
Functions for finding install-locations.
"""


def usersite():
    """
    Returns the directory where packages are installed for the active user.
    """
    import site

    return site.getusersitepackages()


def envsite():
    """
    Returns the directory where packages are installed for the active environment.

    Beware! This does not work in an IPython session.
    """
    import sysconfig

    try:
        return sysconfig.get_paths()["purelib"]
    except KeyError:
        return sysconfig.get_path("purelib")
