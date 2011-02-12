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
Service router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IService
from zenoss_api.router import TreeRouterBase
from zenoss_api.utils import myArgs

info = {"name": "service",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Service"}


class Service(TreeRouterBase):
    implements(IService)

    # Location + action
    location = 'service_router'
    action = 'ServiceRouter'

    def addClass(self, contextUid, id, posQuery=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def query(self, limit=None, start=None, sort=None, dir=None,
            params=None, history=False, uid=None, criteria=(), **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getTree(self, id='/zport/dmd/Services', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getOrganizerTree(self, id='/zport/dmd/Services, **kw'):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getInfo(self, uid, keys=None, **kw))
        args = myArgs()[0]
        return self._request(args, **kw)

    def setInfo(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getInstances(self, uid, start=0, params=None, limit=50, sort='name',
                    dir='ASC', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def moveServices(self, sourceUids, targetUid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getUnmonitoredStartModes(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getMonitoredStartModes(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
