import os
import logging
import sys
try:
    import multiprocessing
except:
    pass
# nose requires multiprocessing and logging to be initialized before the setup
# call, or we'll get a spurious crash on exit.
from setuptools import setup, find_packages
from setuptools.dist import Distribution


def read(fname):
    '''Utility function to read the README file.'''
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

Distribution(dict(
    setup_requires=['versioner'],
    dependency_links=['http://pypispandex.in.zillow.net/simple/versioner/']))

from zillow.tools import versioner

# figure out what the install will need
install_requires = ["setuptools >=0.5"]

setup(
    name="setuptools-cmmi",
    version=versioner.get_version(),
    author="padev",
    author_email="padev@zillowgroup.com",
    description="Egg to handle the CMMI custom task in setuptools.",
    license="(C) Zillow, Inc. 2012-",
    keywords="zillow",
    url="https://stash.atl.zillow.net/projects/LIBS/repos/egg.${eggname}/browse",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
    ],
    install_requires=install_requires,
    tests_require=install_requires,
    test_suite="nose.collector"
    )
