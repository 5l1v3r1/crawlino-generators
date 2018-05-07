import logging

from crawlino_core import generator_plugin

log = logging.getLogger("crawlino-generator")


@generator_plugin
def generator_values(*args, **kwargs):
    """This generator produces the values passed as args input"""
    log.debug("Values generator plugin")

    for x in args:
        yield x
