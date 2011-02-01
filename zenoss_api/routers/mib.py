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
