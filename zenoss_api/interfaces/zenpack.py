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
Interface for zenpack router
"""

from zope.interface import Interface


class IZenpack(Interface):

    def getEligiblePacks(self, **kw):
        """
        Get a list of eligible ZenPacks to add to.

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - packs: ([dictionary]) List of objects representing ZenPacks
            - totalCount: (integer) Total number of eligible ZenPacks
        """

    def addToZenPack(self, topack, zenpack):
        """
        Add an object to a ZenPack.

        @type  topack: string
        @param topack: Unique ID of the object to add to ZenPack
        @type  zenpack: string
        @param zenpack: Unique ID of the ZenPack to add object to

            @rtype:   DirectResponse
            @return:  Success message
        """

