import logging
import os

from string import Template

from datetime import datetime
from time import strftime

LOG = logging.getLogger(__name__)


def _load_vars():
    # Load constant vars

    # Not a lot here yet, but we'll add more later.
    return {
        "project_dir": os.getcwd(),
        "date_time": str(datetime.now())
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
    LOG.info("dist: {}".format(dist))
    LOG.info("attr: {}".format(attr))
    LOG.info("url: {}".format(values['url']))
    LOG.info("config-options: {}".format(values['config-options']))


