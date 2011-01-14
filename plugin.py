"""
Code borrowed from twisted's plugin.py - thanks folks
"""

import os
import logging
import sys

from zope.interface import Interface

sys.path.append(os.path.dirname(__file__))


class IPlugin(Interface):
    """
    Interface that must be implented by all routers
    """

class PluginManager:
    definitions = {}


    def __init__(self, folder):
        """Load all available definitions stored in folder"""
        folder = os.path.abspath(folder)

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
            logging.info("Loaded %s" % name)

    def loadSingle(self, name, *args, **kwargs):
        """
        Creates a new instance of a definition
        name - name of the definition to create

        any other parameters passed will be sent to the __init__ function
        of the definition, including those passed by keyword
        """
        print self.definitions
        definition = self.definitions[name]
        return getattr(definition, definition.info["class"])(*args, **kwargs)
