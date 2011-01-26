"""
Interface for messaging router
"""

from zope.interface import Interface


class IMessaging(Interface):
    def getUserMessages(self):
        """
        Get the queued messages for the logged in user.

        @rtype:   dictionary
        @return:  B{Properties}:
            - messages: ([string]) A list of queued messages.
        """
