"""
Interface for nav router
"""

from zope.interface import Interface


class IDetailNav(Interface):

    def getDetailNavConfigs(uid=None, menuIds=None):
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
