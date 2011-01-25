"""
Interface for events router
"""

from zope.interface import Interface


class IEvents(Interface):

    def query(self, limit=0, start=0, sort='lastTime', dir='DESC',
                params=None, history=False, uid=None, criteria=(), **kw):
        """
        Query for events.

        @type  limit: integer
        @param limit: (optional) Max index of events to retrieve (default: 0)
        @type  start: integer
        @param start: (optional) Min index of events to retrieve (default: 0)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return results
            (default: 'lastTime')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'DESC')
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            (default: None)
        @type  history: boolean
        @param history: (optional) True to search the event history table
            instead of active events (default: False)
        @type  uid: string
        @param uid: (optional) Context for the query (default: None)
        @type  criteria: [dictionary]
        @param criteria: (optional) A list of key-value pairs to to build
            query's where clause (default: None)

        @rtype:   dictionary
        @return:  B{Properties}:
            - events: ([dictionary]) List of objects representing events
            - totalCount: (integer) Total count of events returned
            - asof: (float) Current time
        """

    def queryHistory(self, limit, start, sort, dir, params, **kw):
        """
        Query history table for events.

        @type  limit: integer
        @param limit: (optional) Max index of events to retrieve (default: 0)
        @type  start: integer
        @param start: (optional) Min index of events to retrieve (default: 0)
        @type  sort: string
        @param sort: (optional) Key on which to sort the return results
            (default: 'lastTime')
        @type  dir: string
        @param dir: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'DESC')
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            (default: None)

        @rtype:   dictionary
        @return:  B{Properties}:
            - events: ([dictionary]) List of objects representing events
            - totalCount: (integer) Total count of events returned
            - asof: (float) Current time
        """

    def acknowledge(self, evids=None, excludeIds=None, selectState=None,
        field=None, direction=None, params=None, history=False,
        uid=None, asof=None, **kw):
        """
        Acknowledge event(s).

        @type  evids: [string]
        @param evids: (optional) List of event IDs to acknowledge
            (default: None)
        @type  excludeIds: [string]
        @param excludeIds: (optional) List of event IDs to exclude from
            acknowledgment (default: None)
        @type  selectState: string
        @param selectState: (optional) Select event ids based on select state.
            Available values are: All, New, Acknowledged, and
            Suppressed (default: None)
        @type  field: string
        @param field: (optional) Field key to filter gathered events
            (default: None)
        @type  direction: string
        @param direction: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'DESC')
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            (default: None)
        @type  history: boolean
        @param history: (optional) True to use the event history table instead
            of active events (default: False)
        @type  uid: string
        @param uid: (optional) Context for the query (default: None)
        @type  asof: float
        @param asof: (optional) Only acknowledge if there has been no state
            change since this time (default: None)

        @rtype:   DirectResponse
        @return:  Success message
        """

    def unacknowledge(self, evids=None, excludeIds=None, selectState=None,
                        field=None, direction=None, params=None,
                        history=False, uid=None, asof=None, **kw):
        """
        Unacknowledge event(s).

        @type  evids: [string]
        @param evids: (optional) List of event IDs to unacknowledge
            (default: None)
        @type  excludeIds: [string]
        @param excludeIds: (optional) List of event IDs to exclude from
            unacknowledgment (default: None)
        @type  selectState: string
        @param selectState: (optional) Select event ids based on select state.
            Available values are: All, New, Acknowledged, and
            Suppressed (default: None)
        @type  field: string
        @param field: (optional) Field key to filter gathered events (default:
            None)
        @type  direction: string
        @param direction: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'DESC')
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            (default: None)
        @type  history: boolean
        @param history: (optional) True to use the event history table instead
            of active events (default: False)
        @type  uid: string
        @param uid: (optional) Context for the query (default: None)
        @type  asof: float
        @param asof: (optional) Only unacknowledge if there has been no state
            change since this time (default: None)

        @rtype:   DirectResponse
        @return:  Success message
        """

    def reopen(self, evids=None, excludeIds=None, selectState=None, field=None,
                direction=None, params=None, history=False, uid=None,
                asof=None, **kw):
        """
        Reopen event(s).

        @type  evids: [string]
        @param evids: (optional) List of event IDs to reopen (default: None)
        @type  excludeIds: [string]
        @param excludeIds: (optional) List of event IDs to exclude from
            reopen (default: None)
        @type  selectState: string
        @param selectState: (optional) Select event ids based on select state.
            Available values are: All, New, Acknowledged, and
            Suppressed (default: None)
        @type  field: string
        @param field: (optional) Field key to filter gathered events
            (default: None)
        @type  direction: string
        @param direction: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'DESC')
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            (default: None)
        @type  history: boolean
        @param history: (optional) True to use the event history table instead
            of active events (default: False)
        @type  uid: string
        @param uid: (optional) Context for the query (default: None)
        @type  asof: float
        @param asof: (optional) Only reopen if there has been no state
            change since this time (default: None)

        @rtype:   DirectResponse
        @return:  Success message
        """

    def close(self, evids=None, excludeIds=None, selectState=None, field=None,
                direction=None, params=None, history=False, uid=None,
                asof=None, **kw):
        """
        Close event(s).

        @type  evids: [string]
        @param evids: (optional) List of event IDs to close (default: None)
        @type  excludeIds: [string]
        @param excludeIds: (optional) List of event IDs to exclude from
            close (default: None)
        @type  selectState: string
        @param selectState: (optional) Select event ids based on select state.
            Available values are: All, New, Acknowledged, and Suppressed
            (default: None)
        @type  field: string
        @param field: (optional) Field key to filter gathered events
            (default: None)
        @type  direction: string
        @param direction: (optional) Sort order; can be either 'ASC' or 'DESC'
            (default: 'DESC')
        @type  params: dictionary
        @param params: (optional) Key-value pair of filters for this search.
            (default: None)
        @type  history: boolean
        @param history: (optional) True to use the event history table instead
            of active events (default: False)
        @type  uid: string
        @param uid: (optional) Context for the query (default: None)
        @type  asof: float
        @param asof: (optional) Only close if there has been no state
            change since this time (default: None)

        @rtype:   DirectResponse
        @return:  Success message
        """

    def detail(self, evid, history=False, **kw):
        """
        Get event details.

        @type  evid: string
        @param evid: Event ID to get details
        @type  history: boolean
        @param history: (optional) True to search the event history table
            instead of active events (default: False)

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - event: ([dictionary]) List containing a dictionary representing
            event details
        """

    def write_log(self, evid=None, message=None, history=False, **kw):
        """
        Write a message to an event's log.

        @type  evid: string
        @param evid: Event ID to log to
        @type  message: string
        @param message: Message to log
        @type  history: boolean
        @param history: (optional) True to use the event history table instead
            of active events (default: False)

        @rtype:   DirectResponse
        @return:  Success message
        """

    def classify(self, evids, evclass, history=False, **kw):
        """
        Associate event(s) with an event class.

        @type  evids: [string]
        @param evids: List of event ID's to classify
        @type  evclass: string
        @param evclass: Event class to associate events to
        @type  history: boolean
        @param history: (optional) True to use the event history table instead
            of active events (default: False)

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - msg: (string) Success/failure message
            - success: (boolean) True if class update successful
        """

    def add_event(self, summary, device, component, severity, evclasskey,
                evclass, **kw):
        """
        Create a new event.

        @type  summary: string
        @param summary: New event's summary
        @type  device: string
        @param device: Device uid to use for new event
        @type  component: string
        @param component: Component uid to use for new event
        @type  severity: string
        @param severity: Severity of new event. Can be one of the following:
            Critical, Error, Warning, Info, Debug, or Clear
        @type  evclasskey: string
        @param evclasskey: The Event Class Key to assign to this event
        @type  evclass: string
        @param evclass: Event class for the new event

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - evid: (string) The id of the created event
        """

    def column_config(self, uid=None, history=False, **kw):
        """
        Get the current event console field column configuration.

        @type  uid: string
        @param uid: (optional) UID context to use (default: None)
        @type  history: boolean
        @param history: (optional) True to use the event history table instead
            of active events (default: False)

        @rtype:   [dictionary]
        @return:  A list of objects representing field columns
        """
