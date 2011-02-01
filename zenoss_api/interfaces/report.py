# Copyright (C) 2011, Endre Karlson
# All rights reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Interface for report router
"""

from zope.interface import Interface


class IReport(Interface):

    def getReportTypes(**kw):
        """
        Get the available report types.

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - menuText: ([string]) Human readable list of report types
            - reportTypes: ([string]) A list of the available report types
        """

    def addNode(nodeType, contextUid, id, **kw):
        """
        Add a new report or report organizer.

        @type  nodeType: string
        @param nodeType: Type of new node. Can either be 'organizer' or one of
            the report types returned from getReportTypes()
        @type  contextUid: string
        @param contextUid: The organizer where the new node should be added
        @type  id: string
        @param id: The new node's ID

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - tree: (dictionary) Object representing the new Reports tree
            - newNode: (dictionary) Object representing the added node
        """

    def deleteNode(uid, **kw):
        """
        Remove a report or report organizer.

        @type  uid: string
        @param uid: The UID of the node to delete

        @rtype:   [dictionary]
        @return:  B{Properties}:
            - tree: (dictionary) Object representing the new Reports tree
        """

    def moveNode(uids, target, **kw):
        """
        Move a report or report organizer from one organizer to another.

        @type  uids: [string]
        @param uids: The UID's of nodes to move
        @type  target: string
        @param target: The UID of the target Report organizer

        @rtype:   [dictionary]
        @return:  B{Properties}:
            - tree: (dictionary) Object representing the new Reports tree
            - newNode: (dictionary) Object representing the moved node
        """
