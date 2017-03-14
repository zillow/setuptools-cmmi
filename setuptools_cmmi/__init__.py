import logging

import sys

LOG = logging.getLogger(__name__)


def _getvalue(values, paramName):
    val = values[paramName]
    pass


def cmmi_entry_point(dist, attr, values):
    logging.basicConfig()
    LOG.setLevel(logging.DEBUG)

    url_val = _getvalue(values, 'url')
    LOG.info("dist: {}".format(dist))
    LOG.info("attr: {}".format(attr))
    LOG.info("CMMI: {}".format(values))


