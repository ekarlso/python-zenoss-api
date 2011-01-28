"""
Messaging router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IMessaging
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "messaging",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Messaging"}


class Messaging(RouterBase):
    implements(IMessaging)

    # Location + action
    location = 'messaging_router'
    action = 'MessagingRouter'

    def getUserMessages(self, **kw):
        self._request(**kw)
