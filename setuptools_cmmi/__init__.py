import logging

LOG = logging.getLogger(__name__)


def cmmi_entry_point(dist, attr, value):
    logging.basicConfig()
    LOG.setLevel(logging.DEBUG)

    LOG.debug("CMMI BABY!!!!!!!!")
    #version = get_version(**value)
