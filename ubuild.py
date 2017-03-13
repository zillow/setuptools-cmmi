from uranium import current_build

current_build.config.set_defaults({
    "package_name": "setuptools-cmmi",
    "module": "setuptools_cmmi",
    "test_packages": {
        "mock": None,
    },
})

current_build.include("https://stash.atl.zillow.net/projects/LIBS/repos/egg.zillow-uranium/browse/zillow_base.py?raw=true",
                      cache=True)
from zillow_uranium import setup_egg
setup_egg(current_build)
# how do I customize? see:
# https://stash.atl.zillow.net/projects/LIBS/repos/egg.zillow-uranium/browse
# http://uranium.readthedocs.io/en/latest/
