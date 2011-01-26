"""
Process router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IProcess
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "process",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Process"}


class Process(RouterBase):
    implements(IProcess)

    # Location + action
    location = 'process_router'
    action = 'ProcessRouter'

    def moveProcess(self, uid, targetUid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getInfo(self, uid, keys=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setInfo(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getInstances(self, uid, start=0, params=None, limit=50, sort='name',
                    dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getSequence(self):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setSequence(self, uids, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
