    """
Device router for the Zenoss JSON API
"""

from zenoss_api.router import RouterBase


info = {"name": "events",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Events"}


class Events(RouterBase):
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
                    uid=None, asof=None):
        args = myArgs()[0]
        return self._request(args, **kw)

    def reopen(self, evids=None, excludeIds=None, selectState=None,
                field=None, direction=None, params=None, history=False,
                uid=None, asof=None):
        args = myArgs()[0]
        return self._request(args, **kw)

    def close(self, evids=None, excludeIds=None, selectState=None, field=None,
                direction=None, params=None, history=False, uid=None,
                asof=None):
        args = myArgs()[0]
        return self._request(args, **kw)

    def detail(self, evid, history=False):
        args = myArgs()[0]
        return self._request(args, **kw)

    def write_log(self, evid=None, message=None, history=False):
        args = myArgs()[0]
        return self._request(args, **kw)

    def classify(self, evids, evclass, history=False):
        args = myArgs()[0]
        return self._request(args, **kw)

    def add_event(self, summary, device, component, severity, evclasskey,
                evclass):
        args = myArgs()[0]
        return self._request(args, **kw)

    def column_config(self, uid=None, history=False):
        args = myArgs()[0]
        return self._request(args, **kw)
