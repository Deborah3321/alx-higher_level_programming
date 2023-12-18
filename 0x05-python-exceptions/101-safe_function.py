#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        new = fct(*args)
    except BaseException as e:
        new = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return new
