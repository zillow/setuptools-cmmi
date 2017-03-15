from setuptools import find_packages


def rebuild_package(package, dest_dir):
    """Open up the package and run setup.py on it with lib and include dirs reset."""
    pkg = find_packages(include=package)

    print "PKGS: {}".format(pkg)
