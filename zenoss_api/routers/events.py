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
Device router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IEvents
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs


info = {"name": "events",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Events"}


class Events(RouterBase):
    implements(IEvents)

    # Location + action
    location = 'evconsole_router'
    action = 'EventsRouter'

    def query(self, limit=0, start=0, sort='lastTime', dir='DESC',
                params=None, history=False, uid=None, criteria=()):
        args = myArgs()[0]
        return self._request(args, **kw)

    def queryHistory(self, limit, start, sort, dir, params, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def acknowledge(self, evids=None, excludeIds=None, selectState=None,
                    field=None, direction=None, params=None, history=False,
                    uid=None, asof=None):
        args = myArgs()[0]
        return self._request(args, **kw)

    def unacknowledge(self, evids=None, excludeIds=None, selectState=None,
                    field=None, direction=None, params=None, history=False,
                    uid=None, asof=None, **):
        args = myArgs()[0]
        return self._request(args, **kw)

    def reopen(self, evids=None, excludeIds=None, selectState=None,
                field=None, direction=None, params=None, history=False,
                uid=None, asof=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def close(self, evids=None, excludeIds=None, selectState=None, field=None,
                direction=None, params=None, history=False, uid=None,
                asof=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def detail(self, evid, history=False, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def write_log(self, evid=None, message=None, history=False, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def classify(self, evids, evclass, history=False, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def add_event(self, summary, device, component, severity, evclasskey,
                evclass, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def column_config(self, uid=None, history=Falsei, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
