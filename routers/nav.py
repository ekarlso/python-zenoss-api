"""
DetailNav router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import IDetailNav
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "nav",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "DetailNav"}


class DetailNav(RouterBase):
    implements(IDetailNav)

    # Location + action
    location = 'detailnav_router'
    action = 'DetailNavRouter'

    def getDetailNavConfigs(self, uid=None, menuIds=None):
        """
        return a list of Detail navigation configurations. Can be
        used to create navigation links. Format is:
        {
        id: <id of the configuration>,
        'viewName': <view to display>,
        'xtype': <Ext type for the panel>,
        'text': <display name of the config info>
        }
        """

        args = myArgs()[0]
        return self._request(args, **kw)

    def getContextMenus(self, uid):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getSecurityPermissions(self, uid):
        args = myArgs()[0]
        return self._request(args, **kw)
