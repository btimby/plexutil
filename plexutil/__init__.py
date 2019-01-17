import logging
from compat import Log, DATA, DATA_SENTINAL


LOGGER = logging.getLogger(__name__)


def _make_ns_name(name, ns=None):
    '''Create a namespaced name. Used with Plex globals to avoid collisions.'''
    if ns is None:
        return name
    return ns + ':' + name


def set_global(name, value, ns=None):
    '''Sets a server global variable.'''
    if DATA is DATA_SENTINAL:
        Log('DATA is unitialized')

    ns_name = _make_ns_name(name, ns)
    DATA[ns_name] = value


def get_global(name, ns=None):
    '''Gets a server global variable.'''
    if DATA is DATA_SENTINAL:
        Log('DATA is unitialized')

    ns_name = _make_ns_name(name, ns)
    return DATA[ns_name]


def get_global_int(name, ns=None):
    '''Gets a server global variable as an integer.'''
    return int(get_global(name, ns=ns))


def get_global_bool(name, ns=None):
    '''Gets a server global variable as an boolean.'''
    return bool(get_global(name, ns=ns))


def get_global_float(name, ns=None):
    '''Gets a server global variable as an float.'''
    return float(get_global(name, ns=ns))
