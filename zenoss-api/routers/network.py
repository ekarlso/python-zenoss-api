"""
Network router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import INetwork
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "network",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Network"}


class Network(RouterBase):
    implements(INetwork)

    # Location + action
    location = 'network_router'
    action = 'NetworkRouter'


    def discoverDevices(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addNode(self, newSubnet, contextUid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteNode(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getInfo(self, uid, keys=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setInfo(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getIpAddresses(self, uid, start=0, params=None, limit=50, sort='name',
                        order='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
