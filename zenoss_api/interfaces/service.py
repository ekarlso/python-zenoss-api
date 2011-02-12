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
Interface for services router
"""

from zope.interface import Interface


class IService(Interface):

    def addClass(contextUid, id, posQuery=None, **kw):
        """
        Add a new service class.

        @type  contextUid: string
        @param contextUid: Unique ID of the service ogranizer to add new class to
        @type  id: string
        @param id: ID of the new service
        @type  posQuery: dictionary
        @param posQuery: Object defining a query where the returned position will lie

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - newIndex: (integer) Index of the newly added class in the query
            defined by posQuery
        """

    def query(limit=None, start=None, sort=None, dir=None, params=None,
            history=False, uid=None, criteria=(), **kw):
        """
        Retrieve a list of services based on a set of parameters.

        @type  limit: integer
        @param limit: (optional) Number of items to return; used in pagination
            (default: None)
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return results
            (default: None)
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
        @type  history: boolean
        @param history: not used
        @type  uid: string
        @param uid: Service class UID to query
        @type  criteria: list
        @param criteria: not used

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - services: ([dictionary]) List of objects representing services
            - totalCount: (integer) Total number of services
            - hash: (string) Hashcheck of the current services state
            - disabled: (boolean) True if current user cannot manage services
        """

    def getTree(id, **kw):
        """
        Returns the tree structure of an organizer hierarchy.

        @type  id: string
        @param id: Id of the root node of the tree to be returned

        @rtype:   [dictionary]
        @return:  Object representing the tree
        """

    def getOrganizerTree(id, **kw):
        """
        Returns the tree structure of an organizer hierarchy, only including
        organizers.

        @type  id: string
        @param id: Id of the root node of the tree to be returned

        @rtype:   [dictionary]
        @return:  Object representing the organizer tree
        """

    def getInfo(uid, keys=None, **kw):
        """
        Get the properties of a service.

        @type  uid: string
        @param uid: Unique identifier of a service
        @type  keys: list
        @param keys: (optional) List of keys to include in the returned
            dictionary. If None then all keys will be returned
            (default: None)

        @rtype:   DirectResponse
        @return:  B{Properties}
            - data: (dictionary) Object representing a service's properties
            - disabled: (boolean) True if current user cannot manage services
        """

    def setInfo(**kw):
        """
        Set attributes on a service.
        This method accepts any keyword argument for the property that you wish
        to set. The only required property is "uid".

        @type    uid: string
        @keyword uid: Unique identifier of a service

        @rtype:   DirectResponse
        @return:  Success message
        """

    def getInstances(uid, start=0, params=None, limit=50, sort='name',
                    dir='ASC', **kw):
        """
        Get a list of instances for a service UID.

        @type  uid: string
        @param uid: Service UID to get instances of
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: 0)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
        @type  limit: integer
        @param limit: (optional) Number of items to return; used in pagination
            (default: 50)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return results
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects representing service instances
            - totalCount: (integer) Total number of instances
        """

    def moveServices(sourceUids, targetUid, **kw):
        """
        Move service(s) from one organizer to another.

        @type  sourceUids: [string]
        @param sourceUids: UID(s) of the service(s) to move
        @type  targetUid: string
        @param targetUid: UID of the organizer to move to

        @rtype:   DirectResponse
        @return:  Success messsage
        """

    def getUnmonitoredStartModes(uid, **kw):
        """
        Get a list of unmonitored start modes for a Windows service.

        @type  uid: string
        @param uid: Unique ID of a Windows service.

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([string]) List of unmonitored start modes for a Windows service
        """

    def getMonitoredStartModes(uid, **kw):
        """
        Get a list of monitored start modes for a Windows service.

        @type  uid: string
        @param uid: Unique ID of a Windows service.

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([string]) List of monitored start modes for a Windows service
        """
