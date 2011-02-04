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
Interface for network router
"""

from zope.interface import Interface


class INetwork(Interface):

    def discoverDevices(uid, **kw):
        """
        @type  uid: string
        @param uid: Unique identifier of the network to discover

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - jobId: (integer) The id of the discovery job
        """

    def addNode(newSubnet, contextUid, **kw):
        """
        Add a new subnet.

        @type  newSubnet: string
        @param newSubnet: New subnet to add
        @type  contextUid: string
        @param contextUid: Unique identifier of the network parent of the new
            subnet

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - newNode: (dictionary) An object representing the new subnet node
        """

    def deleteNode(uid, **kw):
        """
        Delete a subnet.

        @type  uid: string
        @param uid: Unique identifier of the subnet to delete

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - tree: (dictionary) An object representing the new network tree
        """

    def getTree(id='/zport/dmd/Networks', **kw):
        """
        Returns the tree structure of an organizer hierarchy where
        the root node is the organizer identified by the id parameter.

        @type  id: string
        @param id: Id of the root node of the tree to be returned. Defaults to
            the Networks tree root.

        @rtype:   [dictionary]
        @return:  Object representing the tree
        """

    def getInfo(uid, keys=None, **kw):
        """
        Returns a dictionary of the properties of an object

        @type  uid: string
        @param uid: Unique identifier of an object
        @type  keys: list
        @param keys: (optional) List of keys to include in the returned
            dictionary. If None then all keys will be returned

        @rtype:   DirectResponse
        @return:  B{Properties}
            - data: (dictionary) Object properties
        """

    def setInfo(**kw):
        """
        Main method for setting attributes on a device or device organizer.
        This method accepts any keyword argument for the property that you wish
        to set. The only required property is "uid".

        @type    uid: string
        @keyword uid: Unique identifier of an object

        @rtype: DirectResponse
        """

    def getIpAddresses(uid, start=0, params=None, limit=50, sort='name',
                        order='ASC', **kw):
        """
        Given a subnet, get a list of IP addresses and their relations.

        @type  uid: string
        @param uid: Unique identifier of a subnet
        @type  start: integer
        @param start: Offset to return the results from; used in pagination
        @type  params: string
        @param params: Not used
        @type  limit: integer
        @param limit: Number of items to return; used in pagination
        @type  sort: string
        @param sort: (optional) Key on which to sort the return results;
        defaults to 'name'
        @type  order: string
        @param order: Sort order; can be either 'ASC' or 'DESC'

        @rtype: DirectResponse
        """
