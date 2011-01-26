"""
Code borrowed from twisted's plugin.py - thanks folks
"""

import os
import logging
import sys

from zope.interface import Interface

sys.path.append(os.path.dirname(__file__))


class PluginManager:
    definitions = {}


    def __init__(self, folder):
        """Load all available definitions stored in folder"""

        # Woop, loop through the paths and set the folder to path if folder
        # exists in one of the items in sys.path
        for path in sys.path:
            path = os.path.abspath(path + "/" + folder)
            if os.path.isdir(path):
                folder = path
                break

        # Is it there?
        if not os.path.isdir(folder):
            logging.error(
                "Unable to load plugins because '%s' is not a folder" % folder
                )
            return

        # Append the folder because we need straight access
        sys.path.append(folder)

        # Build list of folders in directory
        to_import = [f for f in os.listdir(folder) if f.endswith(".py")]

        # Do the actual importing
        for module in to_import:
            self.__initialize_def(module)

    def __initialize_def(self, module):
        """Attempt to load the definition"""

        # Import works the same for py files and package modules so strip!
        if module.endswith(".py"):
            name = module [:-3]
        else:
            name = module

        # Do the actual import
        __import__(name)
        definition = sys.modules[name]

        # Add the definition only if the class is available
        if hasattr(definition, definition.info["class"]):
            self.definitions[definition.info["name"]] = definition
            logging.info("Loaded '%s'" % name)

    def loadSingle(self, name, *args, **kw):
        """
        Creates a new instance of a definition
        name - name of the definition to create

        any other parameters passed will be sent to the __init__ function
        of the definition, including those passed by keyword
        """
        logging.info("Loading definition '%s'" % name)
        definition = self.definitions[name]
        if "pathinfo" in kw:
            fp = (definition.__file__, os.path.dirname(definition.__file__))
            kw["path"] = fp
        try:
            instance = getattr(
                definition, definition.info["class"])(*args, **kw)
        except TypeError, e:
            logging.fatal(
                "Failed when loading definition '%s / %s' error - '%s'" %
                    (name, definition, e))
            return None
        except NotImplementedError, e:
            logging.info("Not loading '%s' - not implemented")
            return None

        return instance

    def loadAll(self, *args, **kw):
        """
        Creates an instance of each definition in definitions loaded when the
        manager is instantiated - should only be used if the definitions works
        the same ways.

        returns a dict of {"name": instance}
        params passed to *args and **kw will be passed to each definition
        """
        loaded = {}
        logging.info("Attempting to load up definitions - '%s'" %
            " ".join(self.definitions.keys()))
        for definition in self.definitions.keys():
            loaded[definition] = self.loadSingle(definition, *args, **kw)

        return loaded
