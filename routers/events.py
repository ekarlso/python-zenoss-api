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


    def query(self, args={}):
        args = self._build_args(args)

        return self._request(args)
