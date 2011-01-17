import inspect
import os

def funcW():
    return inspect.stack()[1][3]


def funcParent():
    return inspect.stack()[2][3]
