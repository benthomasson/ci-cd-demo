"""
json_filter.py:   An event filter that filters keys out of events.

Includes override excludes.

This is useful to exclude information from events that is unneeded by the rule engine.
"""

import multiprocessing as mp


import fnmatch


def matches_include_keys(include_keys, s):
    for pattern in include_keys:
        if fnmatch.fnmatch(s, pattern):
            return True
    return False


def matches_exclude_keys(exclude_keys, s):
    for pattern in exclude_keys:
        if fnmatch.fnmatch(s, pattern):
            return True
    return False


def main(event, exclude_keys=[], include_keys=[]):
    logger = mp.get_logger()
    q = []
    q.append(event)
    while q:
        o = q.pop()
        if isinstance(o, dict):
            for i in list(o.keys()):
                if i in include_keys:
                    q.append(o[i])
                elif matches_include_keys(include_keys, i):
                    q.append(o[i])
                elif i in exclude_keys:
                    del o[i]
                elif matches_exclude_keys(exclude_keys, i):
                    del o[i]
                else:
                    q.append(o[i])

    return event
