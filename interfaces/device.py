"""
Interface for devices router
"""

from zope.interface import Interface


class IDevice(Interface):

    def addLocationNode(type, contextUid, id,
                        description=None, address=None, **kw):
        """
        Adds a new location organizer specified by the parameter id to
        the parent organizer specified by contextUid.

        contextUid must be a path to a Location.

        @type  type: string
        @param type: Node type (always 'organizer' in this case)
        @type  contextUid: string
        @param contextUid: Path to the location organizer that will
            be the new node's parent (ex. /zport/dmd/Devices/Locations)
        @type  id: string
        @param id: The identifier of the new node
        @type  description: string
        @param description: (optional) Describes the new location
        @type  address: string
        @param address: (optional) Physical address of the new location

        @rtype:   dictionary
        @return:  B{Properties}:
            - success: (bool) Success of node creation
            - nodeConfig: (dictionary) The new location's properties
        """

    def getTree(id, **kw):
        """
        Returns the tree structure of an organizer hierarchy where
        the root node is the organizer identified by the id parameter.

        @type  id: string
        @param id: Id of the root node of the tree to be returned

        @rtype:   [dictionary]
        @return:  Object representing the tree
        """

    def getComponents(uid=None, meta_type=None,
                       keys=None, start=0, limit=50,
                       sort='name', dir='ASC', name=None, **kw):
        """
        Retrieves all of the components at a given UID. This method
        allows for pagination.

        @type  uid: string
        @param uid: Unique identifier of the device whose components are
            being retrieved
        @type  meta_type: string
        @param meta_type: (optional) The meta type of the components to be
            retrieved (default: None)
        @type  keys: list
        @param keys: (optional) List of keys to include in the returned
            dictionary. If None then all keys will be returned (default: None)
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: 0)
        @type  limit: integer
        @param limit: (optional) Number of items to return; used in pagination
            (default: 50)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return results;
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')
        @type  name: regex
        @param name: (optional) Used to filter the results (default: None)

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: (dictionary) The components returned
            - totalCount: (integer) Number of items returned
            - hash: (string) Hashcheck of the current component state (to check
            whether components have changed since last query)
        """

    def getComponentTree(uid=None, id=None, **kw):
        """
        Retrieves all of the components set up to be used in a
        tree.

        @type  uid: string
        @param uid: Unique identifier of the root of the tree to retrieve
        @type  id: string
        @param id: not used

        @rtype:   [dictionary]
        @return:  Component properties in tree form
        """

    def findComponentIndex(componentUid, uid=None, meta_type=None,
                                sort='name', dir='ASC', name=None, **kw):
        """
        Given a component uid and the component search criteria, this retrieves
        the position of the component in the results.

        @type  componentUid: string
        @param componentUid: Unique identifier of the component whose index
            to return
        @type  uid: string
        @param uid: Unique identifier of the device queried for components
        @type  meta_type: string
        @param meta_type: (optional) The meta type of the components to
            retrieve (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return results
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')
        @type  name: regex
        @param name: (optional) Used to filter the results (default: None)

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - index: (integer) Index of the component
        """

    def getForm(uid, **kw):
        """
        Given an object identifier, this returns all of the editable fields
        on that object as well as their ExtJs xtype that one would
        use on a client side form.

        @type  uid: string
        @param uid: Unique identifier of an object

        @rtype:   DirectResponse
        @return:  B{Properties}
            - form: (dictionary) form fields for the object
        """

    def getInfo(uid, keys=None, **kw):
        """
        Get the properties of a device or device organizer

        @type  uid: string
        @param uid: Unique identifier of an object
        @type  keys: list
        @param keys: (optional) List of keys to include in the returned
            dictionary. If None then all keys will be returned (default: None)

        @rtype:   DirectResponse
        @return:  B{Properties}
            - data: (dictionary) Object properties
            - disabled: (bool) If current user doesn't have permission to use
            setInfo
        """

    def setInfo(uid, **kw):
        """
        Set attributes on a device or device organizer.
        This method accepts any keyword argument for the property that you wish
        to set. The only required property is "uid".

        @type    uid: string
        @param uid: Unique identifier of an object

        @rtype: DirectResponse
        """

    def setProductInfo(uid, **kw):
        """
        Sets the ProductInfo on a device. This method has the following valid
        keyword arguments:

        @type    uid: string
        @param uid: Unique identifier of a device

        @type    hwManufacturer: string
        @keyword hwManufacturer: Hardware manufacturer
        @type    hwProductName: string
        @keyword hwProductName: Hardware product name
        @type    osManufacturer: string
        @keyword osManufacturer: Operating system manufacturer
        @type    osProductName: string
        @keyword osProductName: Operating system product name
        @rtype:  DirectResponse
        """

    def getDevices(uid=None, start=0, params=None, limit=50,
                        sort='name', dir='ASC', **kw):
        """
        Retrieves a list of devices. This method supports pagination.

        @type  uid: string
        @param uid: Unique identifier of the organizer to get devices from
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: 0)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress, deviceClass, or
            productionState (default: None)
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
            - devices: (list) Dictionaries of device properties
            - totalCount: (integer) Number of devices returned
            - hash: (string) Hashcheck of the current device state (to check
            whether devices have changed since last query)
        """

    def moveDevices(uids, target, hashcheck, ranges=(), uid=None,
                        params=None, sort='name', dir='ASC', **kw):
        """
        Moves the devices specified by uids to the organizer specified by
        'target'.

        @type  uids: [string]
        @param uids: List of device uids to move
        @type  target: string
        @param target: Uid of the organizer to move the devices to
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress,
        deviceClass, or productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - tree: ([dictionary]) Object representing the new device tree
            - exports: (integer) Number of devices moved
        """

    def pushChanges(uids, hashcheck, ranges=(), uid=None, params=None,
                        sort='name', dir='ASC', **kw):
        """
        Push changes on device(s) configuration to collectors.

        @type  uids: [string]
        @param uids: List of device uids to push changes
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress, deviceClass, or
            productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  Success message
        """

    def lockDevices(uids, hashcheck, ranges=(), updates=False,
                            deletion=False, sendEvent=False, uid=None,
                            params=None, sort='name', dir='ASC', **kw):
        """
        Lock device(s) from changes.

        @type  uids: [string]
        @param uids: List of device uids to lock
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  updates: boolean
        @param updates: (optional) True to lock device from updates
            (default: False)
        @type  deletion: boolean
        @param deletion: (optional) True to lock device from deletion
            (default: False)
        @type  sendEvent: boolean
        @param sendEvent: (optional) True to send an event when an action is
            blocked by locking (default: False)
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress, deviceClass, or
            productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def resetIp(uids, hashcheck, uid=None, ranges=(), params=None,
                sort='name', dir='ASC', ip='', **kw):
        """
        Reset IP address(es) of device(s) to the results of a DNS lookup or
        a manually set address

        @type  uids: [string]
        @param uids: List of device uids with IP's to reset
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress, deviceClass, or
            productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')
        @type  ip: string
        @param ip: (optional) IP to set device to. Empty string causes DNS
            lookup (default: '')
        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def resetCommunity(uids, hashcheck, uid=None, ranges=(), params=None,
                        sort='name', dir='ASC', **kw):
        """
        Reset SNMP community string(s) on device(s)

        @type  uids: [string]
        @param uids: List of device uids to reset
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress,
            deviceClass, or productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def setProductionState(uids, prodState, hashcheck, uid=None,
                            ranges=(), params=None, sort='name',
                            dir='ASC', **kw):
        """
        Set the production state of device(s)

        @type  uids: [string]
        @param uids: List of device uids to set
        @type  prodState: integer
        @param prodState: Production state to set device(s) to.
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress,
            deviceClass, or productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def setPriority(uids, priority, hashcheck, uid=None, ranges=(),
                    params=None, sort='name', dir='ASC', **kw):
        """
        Set device(s) priority.

        @type  uids: [string]
        @param uids: List of device uids to set
        @type  priority: integer
        @param priority: Priority to set device(s) to.
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress,
            deviceClass, or productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def setCollector(uids, collector, hashcheck, uid=None, ranges=(),
                    params=None, sort='name', dir='ASC', **kw):
        """
        Set device(s) collector.

        @type  uids: [string]
        @param uids: List of device uids to set
        @type  collector: string
        @param collector: Collector to set devices to
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress, deviceClass, or
            productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def setComponentsMonitored(uids, hashcheck, monitor=False,
                                uid=None, ranges=(), meta_type=None,
                                keys=None, start=0, limit=50, sort='name',
                                dir='ASC', name=None):
        """
        Set the monitoring flag for component(s)

        @type  uids: [string]
        @param uids: List of component uids to set
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the components (from getComponents())
        @type  monitor: boolean
        @param monitor: (optional) True to monitor component (default: False)
        @type  uid: string
        @param uid: (optional) Device to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  meta_type: string
        @param meta_type: (optional) The meta type of the components to
            retrieve (default: None)
        @type  keys: [string]
        @param keys: not used
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: 0)
        @type  limit: integer
        @param limit: (optional) Number of items to return; used in pagination
            (default: 50)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')
        @type  name: string
        @param name: (optional) Component name to search for when loading
            ranges (default: None)

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def lockComponents(uids, hashcheck, uid=None, ranges=(),
                        updates=False, deletion=False, sendEvent=False,
                        meta_type=None, keys=None, start=0, limit=50,
                        sort='name', dir='ASC', name=None, **kw):
        """
        Lock component(s) from changes.

        @type  uids: [string]
        @param uids: List of component uids to lock
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the components (from getComponents())
        @type  uid: string
        @param uid: (optional) Device to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  updates: boolean
        @param updates: (optional) True to lock component from updates
            (default: False)
        @type  deletion: boolean
        @param deletion: (optional) True to lock component from deletion
            (default: False)
        @type  sendEvent: boolean
        @param sendEvent: (optional) True to send an event when an action is
            blocked by locking (default: False)
        @type  meta_type: string
        @param meta_type: (optional) The meta type of the components to
            retrieve (default: None)
        @type  keys: [string]
        @param keys: not used
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: 0)
        @type  limit: integer
        @param limit: (optional) Number of items to return; used in pagination
            (default: 50)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')
        @type  name: string
        @param name: (optional) Component name to search for when loading
            ranges (default: None)

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def deleteComponents(uids, hashcheck, uid=None, ranges=(),
                        meta_type=None, keys=None, start=0, limit=50,
                        sort='name', dir='ASC', name=None, **kw):
        """
        Delete device component(s).

        @type  uids: [string]
        @param uids: List of component uids to delete
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the components (from getComponents())
        @type  uid: string
        @param uid: (optional) Device to use when using ranges to get
            additional uids (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  meta_type: string
        @param meta_type: (optional) The meta type of the components to
            retrieve (default: None)
        @type  keys: [string]
        @param keys: not used
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: 0)
        @type  limit: integer
        @param limit: (optional) Number of items to return; used in pagination
            (default: 50)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')
        @type  name: string
        @param name: (optional) Component name to search for when loading
            ranges (default: None)

        @rtype:   DirectResponse
        @return:  Success or failure message
        """

    def removeDevices(uids, hashcheck, action="remove", uid=None,
                            ranges=(), params=None, sort='name', dir='ASC',
                            **kw):
        """
        Remove/delete device(s).

        @type  uids: [string]
        @param uids: List of device uids to remove
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  action: string
        @param action: Action to take. 'remove' to remove devices from
            organizer uid, and 'delete' to delete the device from Zenoss.
        @type  uid: string
        @param uid: (optional) Organizer to use when using ranges to get
            additional uids and/or to remove device (default: None)
        @type  ranges: [integer]
        @param ranges: (optional) List of two integers that are the min/max
            values of a range of uids to include (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress,
            deviceClass, or productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - devtree: ([dictionary]) Object representing the new device tree
            - grptree: ([dictionary]) Object representing the new group tree
            - systree: ([dictionary]) Object representing the new system tree
            - loctree: ([dictionary]) Object representing the new location tree
        """

    def getEvents(uid, **kw):
        """
        Get events for a device.

        @type  uid: [string]
        @param uid: Device to get events for

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of events for a device
        """

    def loadRanges(ranges, hashcheck, uid=None, params=None,
                    sort='name', dir='ASC', **kw):
        """
        Get a range of device uids.

        @type  ranges: [integer]
        @param ranges: List of two integers that are the min/max values of a
            range of uids
        @type  hashcheck: string
        @param hashcheck: Hashcheck for the devices (from getDevices())
        @type  uid: string
        @param uid: (optional) Organizer to use to get uids (default: None)
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            Can be one of the following: name, ipAddress,
            deviceClass, or productionState (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')

        @rtype:   [string]
        @return:  A list of device uids
        """

    def loadComponentRanges(ranges, hashcheck, uid=None, types=(),
                            meta_type=(), start=0, limit=None,
                            sort='name', dir='ASC', name=None, **kw):
        """
        Get a range of component uids.

        @type  ranges: [integer]
        @param ranges: List of two integers that are the min/max values of a
            range of uids
        @type  hashcheck: string
        @param hashcheck: not used
        @type  uid: string
        @param uid: (optional) Device to use to get uids (default: None)
        @type  types: [string]
        @param types: (optional) The types of components to retrieve
            (default: None)
        @type  meta_type: string
        @param meta_type: (optional) The meta type of the components to
            retrieve (default: None)
        @type  start: integer
        @param start: (optional) Offset to return the results from; used in
            pagination (default: 0)
        @type  limit: integer
        @param limit: (optional) Number of items to return; used in pagination
            (default: None)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return result
            (default: 'name')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'ASC')
        @type  name: string
        @param name: (optional) Component name to search for when loading
            ranges (default: None)
        @rtype:   [string]
        @return:  A list of component uids
        """

    def getUserCommands(uid, **kw):
        """
        Get a list of user commands for a device uid.

        @type  uid: string
        @param uid: Device to use to get user commands

        @rtype:   [dictionary]
        @return:  List of objects representing user commands
        """

    def getProductionStates(**kw):
        """
        Get a list of available production states.

        @rtype:   [dictionary]
        @return:  List of name/value pairs of available production states
        """

    def getPriorities(**kw):
        """
        Get a list of available device priorities.

        @rtype:   [dictionary]
        @return:  List of name/value pairs of available device priorities
        """

    def getCollectors(**kw):
        """
        Get a list of available collectors.

        @rtype:   [string]
        @return:  List of collectors
        """

    def getDeviceClasses(**kw):
        """
        Get a list of all device classes.

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - deviceClasses: ([dictionary]) List of device classes
            - totalCount: (integer) Total number of device classes
        """

    def getManufacturerNames(**kw):
        """
        Get a list of all manufacturer names.

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - manufacturers: ([dictionary]) List of manufacturer names
            - totalCount: (integer) Total number of manufacturer names
        """

    def getHardwareProductNames(manufacturer='', **kw):
        """
        Get a list of all hardware product names from a manufacturer.

        @type  manufacturer: string
        @param manufacturer: Manufacturer name

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - productNames: ([dictionary]) List of hardware product names
            - totalCount: (integer) Total number of hardware product names
        """

    def getOSProductNames(manufacturer='', **kw):
        """
        Get a list of all OS product names from a manufacturer.

        @type  manufacturer: string
        @param manufacturer: Manufacturer name

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - productNames: ([dictionary]) List of OS product names
            - totalCount: (integer) Total number of OS product names
        """

    def addDevice(deviceName, deviceClass, title=None,
                    snmpCommunity="", snmpPort=161,
                    model=False, collector='localhost', rackSlot=0,
                    productionState=1000, comments="", hwManufacturer="",
                    hwProductName="", osManufacturer="", osProductName="",
                    priority=3, tag="", serialNumber="", **kw):
        """
        Add a device.

        @type  deviceName: string
        @param deviceName: Name or IP of the new device
        @type  deviceClass: string
        @param deviceClass: The device class to add new device to
        @type  title: string
        @param title: (optional) The title of the new device (default: '')
        @type  snmpCommunity: string
        @param snmpCommunity: (optional) A specific community string to use for
            this device. (default: '')
        @type  snmpPort: integer
        @param snmpPort: (optional) SNMP port on new device
            (default: 161)
        @type  model: boolean
        @param model: (optional) True to model device at add time
            (default: False)
        @type  collector: string
        @param collector: (optional) Collector to use for new device
            (default: localhost)
        @type  rackSlot: string
        @param rackSlot: (optional) Rack slot description
            (default: '')
        @type  productionState: integer
        @param productionState: (optional) Production state of the new device
            (default: 1000)
        @type  comments: string
        @param comments: (optional) Comments on this device
            (default: '')
        @type  hwManufacturer: string
        @param hwManufacturer: (optional) Hardware manufacturer name
            (default: '')
        @type  hwProductName: string
        @param hwProductName: (optional) Hardware product name (default: '')
        @type  osManufacturer: string
        @param osManufacturer: (optional) OS manufacturer name (default: '')
        @type  osProductName: string
        @param osProductName: (optional) OS product name (default: '')
        @type  priority: integer
        @param priority: (optional) Priority of this device (default: 3)
        @type  tag: string
        @param tag: (optional) Tag number of this device (default: '')
        @type  serialNumber: string
        @param serialNumber: (optional) Serial number of this device
            (default: '')
        @rtype:   DirectResponse
        @return:  B{Properties}:
            - jobId: (string) ID of the add device job
        """

    def addLocalTemplate(deviceUid, templateId, **kw):
        """
        Adds a local template on a device.

        @type  deviceUid: string
        @param deviceUid: Device uid to have local template
        @type  templateId: string
        @param templateId: Name of the new template

        @rtype:  DirectResponse
        @return: Success message
        """

    def removeLocalTemplate(deviceUid, templateUid, **kw):
        """
        Removes a locally defined template on a device.

        @type  deviceUid: string
        @param deviceUid: Device uid that has local template
        @type  templateUid: string
        @param templateUid: Name of the template to remove

        @rtype:  DirectResponse
        @return: Success message
        """

    def getLocalTemplates(uid, query=None, **kw):
        """
        Get a list of locally defined templates on a device.

        @type  query: string
        @param query: not used
        @type  uid: string
        @param uid: Device uid to query for templates
        @rtype:   DirectResponse
        @return:  B{Properties}:
        - data: ([dictionary]) List of objects representing local templates
        """

    def getTemplates(id, **kw):
        """
        Get a list of available templates for a device.

        @type  id: string
        @param id: Device uid to query for templates
        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects representing templates
        """

    def getUnboundTemplates(uid):
        """
        Get a list of unbound templates for a device.

        @type  uid: string
        @param uid: Device uid to query for templates

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects representing templates
        """

    def getBoundTemplates(uid, **kw):
        """
        Get a list of bound templates for a device.

        @type  uid: string
        @param uid: Device uid to query for templates

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects representing templates
        """

    def setBoundTemplates(uid, templateIds, **kw):
        """
        Set a list of templates as bound to a device.

        @type  uid: string
        @param uid: Device uid to bind templates to
        @type  templateIds: [string]
        @param templateIds: List of template uids to bind to device

        @rtype:   DirectResponse
        @return:  Success message
        """

    def resetBoundTemplates(uid, **kw):
        """
        Remove all bound templates from a device.

        @type  uid: string
        @param uid: Device uid to remove bound templates from

        @rtype:   DirectResponse
        @return:  Success message
        """

    def bindOrUnbindTemplate(uid, templateUid, **kw):
        """
        Bind an unbound template or unbind a bound template from a device.

        @type  uid: string
        @param uid: Device uid to bind/unbind template
        @type  templateUid: string
        @param templateUid: Template uid to bind/unbind

        @rtype:   DirectResponse
        @return:  Success message
        """

    def getOverridableTemplates(uid, query=None, **kw):
        """
        Get a list of available templates on a device that can be overridden.

        @type  query: string
        @param query: not used
        @type  uid: string
        @param uid: Device to query for overridable templates

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects representing templates
        """

    def clearGeocodeCache():
        """
        Clear the Google Maps geocode cache.

        @rtype:   DirectResponse
        @return:  Success message
        """
