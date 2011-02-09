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

import json
import os.path
import logging
import re
import urllib
import urllib2

from zenoss_api import plugin, routers, utils
from zope.interface import Interface, implements


class IRouterBase(Interface):
    """
    Base interface for all router plugins
    """

class ITreeRouterBase(Interface):
    """
    Class for Treed routers"
    """

    def addNode(type, contextUid, id, description=None, **kw):
        """
        Add a node to the existing tree underneath the node specified
        by the context UID

        @type  type: string
        @param type: Either 'class' or 'organizer'
        @type  contextUid: string
        @param contextUid: Path to the node that will
            be the new node's parent (ex. /zport/dmd/Devices)
        @type  id: string
        @param id: Identifier of the new node, must be unique in the
        parent context
        @type  description: string
        @param description: (optional) Describes this new node (default: None)

        @rtype:   dictionary
        @return:  Marshaled form of the created node
        """

    def deleteNode(uid, **kw):
        """
        Deletes a node from the tree.

        B{NOTE}: You can not delete a root node of a tree

        @type  uid: string
        @param uid: Unique identifier of the node we wish to delete

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - msg: (string) Status message
        """

    def moveOrganizer(targetUid, organizerUid, **kw):
        """
        Move the organizer uid to be underneath the organizer
        specified by the targetUid.

        @type  targetUid: string
        @param targetUid: New parent of the organizer
        @type  organizerUid: string
        @param organizerUid: The organizer to move

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: (dictionary) Moved organizer
        """


class RouterBase(object):
    """
    Base for every router - has some common settings and functions
    """
    implements(IRouterBase)

    action = None
    location = None

    def __init__(self, router, *args, **kw):
        """
        Init's the router.. takes a Router instance as arg + args + kw
        """
        # Set up cls name, module name and pathinfo (if received from parent)
        self._cls = self.__class__.__name__
        self._module = self.__module__
        self._path = kw.get("path", None)

        # Router passed from parent
        self._router = router

    def _check_args(func):
        """
        Build / check the args before running a call
        """

        def wrapped(self, args, **kw):
            """"
            This is the function that's called from a router inheriting the
            base, it takes this:

            args:
                The args from the callee containing the data that will be
                passed onto _request as args
            keywords:
                method: What method will be used for the request
            """
            # Log it all
            logging.info("Arguments: '%s' || Keywords: '%s'" % (args, kw))

            # Arguments are none? Set it to a dict
            if args is None:
                args = {}

            method = kw.get("method", utils.funcParent())

            for key, val in args.copy().iteritems():
                if val is None:
                    args.pop(key)

            return func(self, args, method)
        return wrapped

    @_check_args
    def _request(self, args, method):
        """
        Deals with the request - executes self._router._request to get the
        results

        Sets up args etc before passing then to the parent _request
        """
        data = {
            "location": self.location,
            "action": self.action,
            "method": method,
            "data": [args]}

        logging.debug("Router Arguments '%s'" % data)

        resp = None
        try:
            resp = self._router._request(data)
        except urllib2.HTTPError, e:
            print e

        return resp


class Router(object):
    """
    The router itself, has "Subrouters" which are set as attributes in it.
    """

    _authenticated = 0
    _transactions = 0
    _content = "Content-type', 'application/json; charset=utf-8"

    def __init__(self, user, password, **kw):
        # Load all the routers..

        dmdloc = kw.get("dmdloc", "/zport/dmd/")
        url = kw.get("url", "http://localhost:8080/")

        obj = routers.Routers(self, pathinfo=True)
        data = obj.routers()
        for i in data:
            self._setattr(i, data[i])

        # Setup url + dmdloc - http://x.com + /zenport/dmd/
        (self.url, self.dmdloc) = url, dmdloc
        (self.user, self.password) = user, password

        # Set opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.opener.add_handler(urllib2.HTTPHandler(debuglevel=1))

    def _process_login(self):
        """
        Login to the Zenoss API
        """
        loginParams = urllib.urlencode(dict(
            __ac_name=self.user,
            __ac_password=self.password,
            submitted='true',
            came_from=self.url + "/" + self.dmdloc))

        logging.info("Logging in to Zenoss '%s'" % self.url)
        self.opener.open(
            self.url + "/zport/acl_users/cookieAuthHelper/login", loginParams)

    def _request(self, args):
        """
        Do a request.
        """
        # Login if not logged in..
        if not self._authenticated:
            self._process_login()


        # Setup some more args..
        args["type"] = "rpc"
        args["tid"] = self._transactions
        if "data" not in args:
            args["data"] = []

        reqdata = json.dumps(args)

        # Increase tid
        self._transactions += 1

        # Construct the url, log it, and make a request
        url = self.url + "/" + self.dmdloc + "/" + args["location"]
        logging.debug("Request url is '%s'" % url)
        req = urllib2.Request(url)

        # Add the Content-type
        req.add_header("Content-type", args.get("content", self._content))

        return json.loads(self.opener.open(req, reqdata).read())

    def _setattr(self, name, value):
        """
        Set an attribute but don't override
        """
        try:
            getattr(self, name)
        except AttributeError:
            try:
                setattr(self, name, value)
            except AttributeError, e:
                logging.error("Failed setting attribute '%s'" % name)

class TreeRouterBase(RouterBase):
    implements(ITreeRouterBase)

    def addNode(self, type, contextUid, id, description=None, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteNode(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def moveOrganizer(self, targetUid, organizerUid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
