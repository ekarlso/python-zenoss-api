"""
Interface for process router
"""

from zope.interface import Interface


class IProcess(Interface):

    def moveProcess(uid, targetUid, **kw):
        """
        Move a process or organizer from one organizer to another.

        @type  uid: string
        @param uid: UID of the process or organizer to move
        @type  targetUid: string
        @param targetUid: UID of the organizer to move to

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - uid
        """

    def getInfo(uid, keys=None, **kw):
        """
        Get the properties of a process.

        @type  uid: string
        @param uid: Unique identifier of a process
        @type  keys: list
        @param keys: (optional) List of keys to include in the returned
            dictionary. If None then all keys will be returned
            (default: None)

        @rtype:   DirectResponse
        @return:  B{Properties}
            - data: (dictionary) Object representing a process's properties
        """

    def setInfo(uid, **kw):
        """
        Set attributes on a process.
        This method accepts any keyword argument for the property that you wish
        to set. The only required property is "uid".

        @type    uid: string
        @keyword uid: Unique identifier of a process

        @rtype:   DirectResponse
        @return:  B{Properties}
            - data: (dictionary) Object representing a process's new properties
        """

    def getInstances(uid, start=0, params=None, limit=50, sort='name',
                    dir='ASC', **kw):
        """
        Get a list of instances for a process UID.

        @type  uid: string
        @param uid: Process UID to get instances of
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
            - data: ([dictionary]) List of objects representing process instances
            - total: (integer) Total number of instances
        """

    def getSequence(**kw):
        """
        Get the current processes sequence.

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects representing processes in
        sequence order
        """

    def setSequence(uids, **kw):
        """
        Set the current processes sequence.

        @type  uids: [string]
        @param uids: The set of process uid's in the desired sequence

        @rtype:   DirectResponse
        @return:  Success message
        """


