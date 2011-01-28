"""
Device router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IDevice
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "device",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Device"}


class Device(RouterBase):
    implements(IDevice)

    # Location + action
    location = 'device_router'
    action = 'DeviceRouter'

    def addLocationNode(self, type, contextUid, id, description=None,
                        address=None, **kw):
        args = myArgs()[0]
        return self._request(kw, **kw)

    def getTree(self, id, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getComponents(self, uid=None, meta_type=None, keys=None, start=0,
                    limit=50, sort='name', dir='ASC', name=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getComponentTree(self, uid=None, id=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def findComponentIndex(self, componentUid, uid=None, meta_type=None,
                            sort='name', dir='ASC', name=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getForm(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getInfo(self, uid, keys=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setInfo(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setProductInfo(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDevices(self, uid=None, start=0, params=None, limit=50,
                    sort='name', dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def moveDevices(self, uids, target, hashcheck, ranges=(), uid=None,
                    params=None, sort='name', dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def pushChanges(self, uids, hashcheck, ranges=(), uid=None, params=None,
                    sort='name', dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def lockDevices(self, uids, hashcheck, ranges=(), updates=False,
                    deletion=False, sendEvent=False, uid=None, params=None,
                    sort='name', dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def resetIp(self, uids, hashcheck, uid=None, ranges=(), params=None,
                sort='name', dir='ASC', ip='', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def resetCommunity(self, uids, hashcheck, uid=None, ranges=(), params=None,
                        sort='name', dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setProctionState(self, uids, prodState, hashcheck, uid=None, ranges=(),
                        params=None, sort='name', dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setPriority(self, uids, priority, hashcheck, uid=None, ranges=(),
                    params=None, sort='name', dir='ASC', *kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setCollector(self, uids, collector, hashcheck, uid=None, ranges=(),
                    params=None, sort='name', dir='ASC'):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setComponentsMonitored(self, uids, hashcheck, monitor=False, uid=None,
                                ranges=(), meta_type=None, keys=None, start=0,
                                limit=50, sort='name', dir='ASC', name=None,
                                **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def lockComponents(self, uids, hashcheck, uid=None, ranges=(),
                        updates=False, deletion=False, sendEvent=False,
                        meta_type=None, keys=None, start=0, limit=50,
                        sort='name', dir='ASC', name=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteComponents(self, uids, hashcheck, uid=None, ranges=(),
                        meta_type=None, keys=None, start=0, limit=50,
                        sort='name', dir='ASC', name=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def removeDevices(self, uids, hashcheck, action="remove", uid=None,
                        ranges=(), params=None, sort='name', dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getEvents(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def loadRanges(self, ranges, hashcheck, uid=None, params=None, sort='name',
                    dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def loadComponentRanges(self, ranges, hashcheck, uid=None, types=(),
                            meta_type=(), start=0, limit=None, sort='name',
                            dir='ASC', name=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getUserCommands(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getProductionStates(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getPriorities(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getCollectors(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDeviceClasses(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getManufacturerNames(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getHardwareProductNames(self, manufacturer='', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getOSProductNames(self, manufacturer='', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addDevice(self, deviceName, deviceClass, title=None, snmpCommunity="",
                    snmpPort=161, model=False, collector='localhost',
                    rackSlot=0, productionState=1000, comments="",
                    hwManufacturer="", hwProductName="", osManufacturer="",
                    osProductName="", priority=3, tag="", serialNumber="",
                    **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addLocalTemplate(self, deviceUid, templateId, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def removeLocalTemplate(self, deviceUid, templateUid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getLocalTemplates(self, id, query=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getTemplates(self, id, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getUnboundTemplates(self, id, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getBoundTemplates(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setBoundTemplates(self, uid, templateIds, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def resetBoundTemplates(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def bindOrUnbindTemplate(self, uid, templateIds, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getOverridableTemplates(self, uid, query=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def clearGeocodeCache(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
