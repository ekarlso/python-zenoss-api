#!/usr/bin/env python

'''
zenoss-api:  Zenoss JSON API
'''

import os, sys

APPDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APPDIR)

from setuptools import setup, find_packages

# zope.interface
install_requires = ["zope.interface>=3.6.1"]

setupOptions = {
    'name': 'zenoss-api',
    'author': "Endre Karlson, Dave Carmean, Eric Plaster",
    'author_email': "",
    'description': "Zenoss JSON API Python Library",
    'long_description': "Zenoss JSON API Python Library",
    'version': "1.0",
    'url': "https://projects.bouvet-ds.net/indefero/p/zenoss-api/",
    'license': "",
    'install_requires': install_requires,
    'packages': find_packages(),
    }


if __name__ == '__main__':
    setup(**setupOptions)


