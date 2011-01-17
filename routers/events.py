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


    def query(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def queryHistory(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def acknowledge(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def unacknowledge(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def reopen(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def close(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def detail(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def write_log(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def classify(self, args=None):
        args = self._build_args(args)
        return self._request(args)

    def add_event(self, args=None):
        args = self._builds_args(args)
        return self._request(args)

    def column_config(self, args=None):
        args = self._builds_args(args)
        return self._request(args)
