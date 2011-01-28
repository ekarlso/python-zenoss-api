"""
Report router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IReport
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "report",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Report"}


class Report(RouterBase):
    implements(IReport)

    # Location + action
    location = 'report_router'
    action = 'ReportRouter'

    def getReportTypes(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addNode(self, nodeType, contextUid, id, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteNode(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def moveNode(self, uids, target, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
