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
Interface for messaging router
"""

from zope.interface import Interface


class IMib(Interface):

    def getTree(id):
        """
        Returns the tree structure of an organizer hierarchy. Default tree
        root is MIBs.

        @type  id: string
        @param id: (optional) Id of the root node of the tree to be
            returned (default: '/zport/dmd/Mibs')

        @rtype:   [dictionary]
        @return:  Object representing the tree
        """
