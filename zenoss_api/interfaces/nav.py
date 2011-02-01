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
