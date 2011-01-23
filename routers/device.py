"""
Device router for the Zenoss JSON API
"""

from zenoss_api.router import RouterBase
from zenoss_api.interfaces import IDevice
from zenoss_api.utils import myArgs

info = {"name": "device",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Device"}


class Device(RouterBase):
    # Location + action
    location = 'device_router'
    action = 'DeviceRouter'

    def addLocationNode(self, type, contentUid, id, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getTree(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getComponents(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getComponentTree(self, componentUid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def findComponentIndex(self, componentUid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def getForm(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getInfo(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def setInfo(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def setProductInfo(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getDevices(self, **kw):
        return self._request(
            kw, std={'start': 0, 'limit': 50, 'sort': 'name', 'dir': 'ASC'})

    def moveDevices(self, uids, target, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def pushChanges(self, uids, target, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def lockDevices(self, uids, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'updates': False, 'deletion': False,
                            'sendevent': False, 'sort': 'name', 'dir': 'ASC'})

    def resetIp(self, uids, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC', 'ip': ''})

    def resetCommunity(self, uids, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def setProctionState(self, uids, prodState, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def setPriority(self, uids, priority, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def setCollector(self, uids, priority, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def setComponentsMonitored(self, uids, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'monitor': False, 'start': 0,
                            'limit': 50, 'sort': 'name', 'dir': 'ASC'})

    def lockComponents(self, uids, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'updates': False, 'deletion': False,
                            'sendEvent': False, 'start': 0, 'limit': 50,
                            'sort': 'name', 'dir': 'ASC'})

    def deleteComponents(self, uids, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'start': 0, 'limit': 50, 'sort': 'name',
                            'dir': 'ASC'})

    def getEvents(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def loadRanges(self, ranges, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'sort': 'name', 'dir': 'ASC'})

    def loadComponentRanges(self, ranges, hashcheck, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'start': 0, 'sort': 'name',
                            'dir': 'ASC'})

    def getUserCommands(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getProductionStates(self, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getPriorities(self, **kw):
        return self._request(kw)

    def getCollectors(self, **kw):
        return self._request(kw)

    def getDeviceClasses(self, **kw):
        return self._request(kw)

    def getManufacturerNames(self, **kw):
        return self._request(kw)

    def getHardwareProductNames(self, **kw):
        return self._request(kw, std={'manufacturer': ''})

    def getOSProductNames(self, **kw):
        return self._request(kw, std={'manufacturer': ''})

    def addDevice(self, deviceName, deviceClass, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'snmpCommunity': '', 'snmpPort': 161,
            'collector': 'localhost', 'rackSlot': 0, 'productionstate': 1000,
            'comments': '', 'hwManufacturer': '', 'hwProductName': '',
            'osManufacturer': '', 'osProductName': '', 'priority': 3, 'tag': '',
            'serialNumber': ''})

    def addLocalTemplate(self, deviceUid, templateId, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def removeLocalTemplate(self, deviceUid, templateId, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getLocalTemplates (self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'query': False})

    def getTemplates(self, id, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getUnboundTemplates(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getBoundTemplates(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def setBoundTemplates(self, uid, templateIds, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def resetBoundTemplates(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def bindOrUnbindTemplate(self, uid, templateIds, **kw):
        kw.update(myArgs()[0])
        return self._request(kw)

    def getOverridableTemplates(self, uid, **kw):
        kw.update(myArgs()[0])
        return self._request(kw, std={'query': False})

    def clearGeocodeCache(self, **kw):
        return self._request(kw)
