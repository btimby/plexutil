import logging


DATA_SENTINAL = dict()
LOGGER = logging.getLogger(__name__)


def _detect_plex():
    '''Detect plex runtime.'''
    # TODO: make this more complete.
    if 'Log' not in globals():
        return False


if not _detect_plex():

    # Make linter happy and provide a means to test if DATA is valid or not.
    DATA = DATA_SENTINAL

    def Log(msg):
        LOGGER.debug(msg)
