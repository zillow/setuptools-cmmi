import logging
import os
from distutils.errors import DistutilsSetupError

from string import Template

from datetime import datetime
from time import strftime

from setuptools_cmmi.process_cmmi import process_cmmi

LOG = logging.getLogger(__name__)

KEY_DOWNLOAD_DIR = "download_dir"
KEY_CONFIG_OPTIONS = "config_options"
KEY_URL = "url"
KEY_AUTOGEN = "autogen"
KEY_PATCH = "patch"
KEY_PATCH_OPTIONS = "patch_options"
KEY_TEMP_WORK_DIR = "temp_work_dir"

VAR_PROJECT_DIR = "project_dir"
VAR_DATETIME = "datetime"

def _load_vars():
    # Load constant vars

    # Not a lot here yet, but we'll add more later.
    return {
        VAR_PROJECT_DIR: os.getcwd(),
        VAR_DATETIME: str(datetime.now())
    }


def _substitute_vars(org_values, vars):
    # There has got to be a more pythonic way of doing this...but this will work for now.
    values = {key: Template(val).safe_substitute(vars)
              for (key, val) in org_values.iteritems()}
    return values



def cmmi_entry_point(dist, attr, org_values):
    logging.basicConfig()
    LOG.setLevel(logging.DEBUG)

    vars = _load_vars()

    values = _substitute_vars(org_values, vars)

    # Make sure all the needed vars are defined
    download_dir = values.get(KEY_DOWNLOAD_DIR, vars[VAR_PROJECT_DIR] + "/temp_download")
    temp_work_dir = values.get(KEY_TEMP_WORK_DIR, vars[VAR_PROJECT_DIR] + "/temp_work_cmmi")
    url = values.get(KEY_URL, None)
    config_options = values.get(KEY_CONFIG_OPTIONS, '')
    autogen = values.get(KEY_AUTOGEN, '')

    if not url:
        raise DistutilsSetupError("Required 'url' parameter not specified for cmmi.")

    LOG.debug("dist: {}".format(dist))
    LOG.debug("attr: {}".format(attr))
    LOG.debug("url: {}".format(url))
    LOG.debug("config-options: {}".format(values[KEY_CONFIG_OPTIONS]))

    # TODO: Download file here somewhere and return the full path to the file

    process_cmmi(temp_work_dir, config_options, autogen)

