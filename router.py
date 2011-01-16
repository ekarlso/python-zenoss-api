import json
import os.path
import logging
import re
import urllib
import urllib2

from zenoss_api import plugin, utils
from zope.interface import Interface, implements


#_plugins = plugin.PluginManager("routers")


class IRouter(Interface):
    """
    Base interface for all router plugins
    """


class RouterBase(object):
    """
    Base for every router - has some common settings and functions
    """
    implements(IRouter)

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

        # Load up defaults from json file
        self._load_argdata()

    def _build_args(self, args):
        """
        Build / check the args before running a call
        """
        # Get argdata
        current = self._get_argdata(utils.funcParent())

        # Let's set the defaults
        for key, val in current["defaults"].iteritems():
            if key not in args:
                args[key] = val
        return args

    def _get_argdata(self, name):
        """
        Get's the defaults for the call
        """
        data = self._argdata.get(name, None)
        return data

    def _load_argdata(self):
        """
        Load the argdata for the router
        """
        # Set the json filename for the defaults for this router, raise an
        # IOError if not there.
        fp = re.sub("\.\w+$", "", self._path[0]) + ".json"
        if not os.path.isfile(fp):
            raise IOError("File for defaults '%s' not found" % fp)

        logging.debug("Loading defaults for '%s'" % self._module)

        # Open and load JSON
        data = open(fp)
        self._argdata = json.load(data)

    def _request(self, args):
        """
        Deals with the request - executes self._router._request to get the
        results

        Sets up args etc before passing then to the parsent _request
        """
        # If no method was given in args set it to the name of the caller
        if "method" not in args:
            method = utils.funcParent()
        else:
            method = args["method"]

        data = {
            "location": self.location,
            "action": self.action,
            "method": method,
            "data": [args]
        }

        logging.info("Arguments are '%s'" % data)

        resp = None
        try:
            resp = self._router._request(data)
        except urllib2.HTTPError, e:
            print e

        return resp


class Router:
    """
    The router itself, has "Subrouters" which are set as attributes in it.
    """

    _authenticated = 0
    _transactions = 0
    _content = "Content-type', 'application/json; charset=utf-8"

    def __init__(self, url, dmdloc, user, password, **kw):
        # Load all the routers..
        loader = plugin.PluginManager("routers")
        self._routers = loader.loadAll(self, pathinfo=True)
        for i in self._routers:
            self._setattr(i, self._routers[i])

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
            __ac_name = self.user,
            __ac_password = self.password,
            submitted = 'true',
            came_from = self.url + "/" + self.dmdloc))

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
        url = self.url + "/" +  self.dmdloc + "/" + args["location"]
        logging.info("Request url is '%s'" % url)
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
