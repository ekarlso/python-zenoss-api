"""
Interface for messaging router
"""

from zope.interface import Interface


class IMib(Interface):

    def getTree(id):
        """
        Returns the tree structure of an organizer hierarchy. Default tree
        root is MIBs.

        @type  id: string
        @param id: (optional) Id of the root node of the tree to be
            returned (default: '/zport/dmd/Mibs')

        @rtype:   [dictionary]
        @return:  Object representing the tree
        """
