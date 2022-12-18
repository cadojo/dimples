"""
Do implementation types match their required interfaces?
"""


def type_server_interface():
    from dimples.servers import PackageServer, download, distribution, versions
    from dimples.servers.pypi import PyPIServer
    from os.path import curdir

    server = PyPIServer()

    download(server, "dimples", location=curdir, version=None)
    distribution(server, "dimples", version=None)
    versions(server, "dimples")
