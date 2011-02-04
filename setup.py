#!/usr/bin/env python

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
zenoss-api:  Zenoss JSON API
"""

import os
import sys

APPDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APPDIR)

from setuptools import setup, find_packages

# zope.interface
install_requires = ["zope.interface>=3.6.1"]

setupOptions = {
    'name': 'zenoss_api',
    'author': "Endre Karlson, Dave Carmean, Eric Plaster",
    'author_email': "",
    'description': "Zenoss JSON API Python Library",
    'long_description': "Zenoss JSON API Python Library",
    'version': "1.0.1",
    'url': "https://projects.bouvet-ds.net/indefero/p/zenoss-api/",
    'license': "",
    'install_requires': install_requires,
    'packages': find_packages(),
    }


if __name__ == '__main__':
    setup(**setupOptions)
