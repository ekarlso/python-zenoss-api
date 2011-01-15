import inspect
import os
import os.path
import time


def walkOn(path, raisewalk=None):
    """
    Returns a dict:
        dc: total directories
        fc: total files
        found: a dict where the dir name is the key and a list with the files
    """
    def error(error):
        raise OSError("Error %s, %s" % (error.errno, error.strerror))

    exists = os.path.exists(path)
    content = {"dc": 0, "fc": 0, "found": {}}

    if exists == True:
        for root, dirs, files in os.walk(path, onerror=raisewalk):
            content["found"][root] = files
            content["dc"] += 1
            content["fc"] += len(files)
    else:
        raise OSError("Couldn't open path for walk: %s" % path)
    return content

def getContent(path):
    """
    Uses walkOn to get a walk of a path and then get's the stat info of each
    file and replaces the file array element with a tuple containing the
    filename and stat object
    """
    content = walkOn(path)
    content["size"] = 0

    for directory in content["found"]:
        files = content["found"][directory]
        for i in range(0, len(files)):
            # Set filename + filepath
            fn = files[i]
            fp = "/".join([directory, fn])

            # Set stat + size
            stat = os.stat(fp)
            content["size"] += stat.st_size

            # Replace the file entry in the array
            files[i] = (fn, stat)
    return content

def funcW():
    return inspect.stack()[1][3]


def funcParent():
    return inspect.stack()[2][3]


def moduleClasses(module):
    """Return a list with tupes containing class name and the module name"""
    clsmembers = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) is False:
            continue

        clsmodname = obj.__module__
        modname = module.__name__

        if clsmodname == modname:
            clsmembers.append([name, modname, obj])

    return clsmembers

