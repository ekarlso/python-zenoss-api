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
