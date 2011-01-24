import inspect
import os

def funcW():
    return inspect.stack()[1][3]


def funcParent():
    return inspect.stack()[2][3]

def myArgs():
    """
    Returns tuple containing dictionary of calling function's
    named arguments and a list of calling function's unnamed
    positional arguments.
    """
    posname, kwname, args = inspect.getargvalues(inspect.stack()[1][0])[-3:]
    posargs = args.pop(posname, [])
    args.update(args.pop(kwname, []))
    # Remove func + self
    for i in ["func", "self"]:
        if i in args:
            args.pop(i)
    return args, posargs
