"""
Mibs router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IMib
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "mib",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Mib"}


class Mib(RouterBase):
    implements(IMib)

    # Location + action
    location = 'mib_router'
    action = 'MibRouter'

    def __init__(self, router, **kw):
        raise NotImplementedError("Not available in Zenoss yet")
