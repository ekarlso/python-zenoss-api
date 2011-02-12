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
Interface for templates router
"""

from zope.interface import Interface


class ITemplate(Interface):

    def getTemplates(id, **kw):
        """
        Get all templates.

        @type  id: string
        @param id: not used

        @rtype:   [dictionary]
        @return:  List of objects representing the templates in tree hierarchy
        """

    def getDeviceClassTemplates(id, **kw):
        """
        Get all templates by device class. This will return a tree where device
        classes are nodes, and templates are leaves.

        @type  id: string
        @param id: not used

        @rtype:   [dictionary]
        @return:  List of objects representing the templates in tree hierarchy
        """

    def getAddTemplateTargets(query, **kw):
        """
        Get a list of available device classes where new templates can be added.

        @type  query: string
        @param query: not used

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects containing an available device
            class UID and a human-readable label for that class
        """

    def addTemplate(id, targetUid, **kw):
        """
        Add a template to a device class.

        @type  id: string
        @param id: Unique ID of the template to add
        @type  targetUid: string
        @param targetUid: Unique ID of the device class to add template to

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - nodeConfig: (dictionary) Object representing the added template
        """

    def deleteTemplate(uid, **kw):
        """
        Delete a template.

        @type  uid: string
        @param uid: Unique ID of the template to delete

        @rtype:   DirectResponse
        @return:  Success message
        """

    def getThresholds(uid, query='', **kw):
        """
        Get the thresholds for a template.

        @type  uid: string
        @param uid: Unique ID of a template
        @type  query: string
        @param query: not used

        @rtype:   [dictionary]
        @return:  List of objects representing representing thresholds
        """

    def getThresholdDetails(uid, **kw):
        """
        Get a threshold's details.

        @type  uid: string
        @param uid: Unique ID of a threshold

        @rtype:   dictionary
        @return:  B{Properties}:
            - record: (dictionary) Object representing the threshold
            - form: (dictionary) Object representing an ExtJS form for the threshold
        """

    def getDataPoints(query, uid, **kw):
        """
        Get a list of available data points for a template.

        @type  query: string
        @param query: not used
        @type  uid: string
        @param uid: Unique ID of a template

        @rtype:   DirectResponse
        @return:  B{Properties}:
            - data: ([dictionary]) List of objects representing data points
        """

    def addDataPoint(dataSourceUid, name, **kw):
        """
        Add a new data point to a data source.

        @type  dataSourceUid: string
        @param dataSourceUid: Unique ID of the data source to add data point to
        @type  name: string
        @param name: ID of the new data point

        @rtype:   DirectResponse
        @return:  Success message
        """

    def addDataSource(templateUid, name, type, **kw):
        """
        Add a new data source to a template.

        @type  templateUid: string
        @param templateUid: Unique ID of the template to add data source to
        @type  name: string
        @param name: ID of the new data source
        @type  type: string
        @param type: Type of the new data source. From getDataSourceTypes()

        @rtype:   DirectResponse
        @return:  Success message
        """

    def getDataSources(id, **kw):
        """
        Get the data sources for a template.

        @type  id: string
        @param id: Unique ID of a template

        @rtype:   [dictionary]
        @return:  List of objects representing representing data sources
        """

    def getDataSourceDetails(uid, **kw):
        """
        Get a data source's details.

        @type  uid: string
        @param uid: Unique ID of a data source

        @rtype:   dictionary
        @return:  B{Properties}:
            - record: (dictionary) Object representing the data source
            - form: (dictionary) Object representing an ExtJS form for the
            data source
        """

    def getDataPointDetails(uid, **kw):
        """
        Get a data point's details.

        @type  uid: string
        @param uid: Unique ID of a data point

        @rtype:   dictionary
        @return:  B{Properties}:
            - record: (dictionary) Object representing the data point
            - form: (dictionary) Object representing an ExtJS form for the
            data point
        """

    def setInfo(**kw):
        """
        Set attributes on an object.
        This method accepts any keyword argument for the property that you wish
        to set. The only required property is "uid".

        @type    uid: string
        @keyword uid: Unique identifier of an object

        @rtype:  DirectResponse
        @return: B{Properties}:
            - data: (dictionary) The modified object
        """

    def addThreshold(**kw):
        """
        Add a threshold.

        @type    uid: string
        @keyword uid: Unique identifier of template to add threshold to
        @type    thresholdType: string
        @keyword thresholdType: Type of the new threshold. From getThresholdTypes()
        @type    thresholdId: string
        @keyword thresholdId: ID of the new threshold
        @type    dataPoints: [string]
        @keyword dataPoints: List of data points to select for this threshold

        @rtype:  DirectResponse
        @return: Success message
        """

    def removeThreshold(uid, **kw):
        """
        Remove a threshold.

        @type  uid: string
        @param uid: Unique identifier of threshold to remove

        @rtype:  DirectResponse
        @return: Success message
        """

    def getThresholdTypes(query, **kw):
        """
        Get a list of available threshold types.

        @type  query: string
        @param query: not used

        @rtype:   [dictionary]
        @return:  List of objects representing threshold types
        """

    def getDataSourceTypes(query, **kw):
        """
        Get a list of available data source types.

        @type  query: string
        @param query: not used

        @rtype:   [dictionary]
        @return:  List of objects representing data source types
        """

    def getGraphs(uid, query=None, **kw):
        """
        Get the graph definitions for a template.

        @type  uid: string
        @param uid: Unique ID of a template
        @type  query: string
        @param query: not used

        @rtype:   [dictionary]
        @return:  List of objects representing representing graphs
        """

    def addDataPointToGraph(dataPointUid, graphUid, includeThresholds=False,
                            **kw):
        """
        Add a data point to a graph.

        @type  dataPointUid: string
        @param dataPointUid: Unique ID of the data point to add to graph
        @type  graphUid: string
        @param graphUid: Unique ID of the graph to add data point to
        @type  includeThresholds: boolean
        @param includeThresholds: (optional) True to include related thresholds
            (default: False)

        @rtype:   DirectResponse
        @return:  Success message
        """

    def getCopyTargets(uid, query='', **kw):
        """
        Get a list of available device classes to copy a template to.

        @type  uid: string
        @param uid: Unique ID of the template to copy
        @type  query: string
        @param query: (optional) Filter the returned targets' names based on this
            parameter (default: '')

        @rtype:   DirectResponse
        @return: B{Properties}:
        - data: ([dictionary]) List of objects containing an available device
        class UID and a human-readable label for that class
        """

    def copyTemplate(uid, targetUid, **kw):
        """
        Copy a template to a device or device class.

        @type  uid: string
        @param uid: Unique ID of the template to copy
        @type  targetUid: string
        @param targetUid: Unique ID of the device or device class to bind to template
        @rtype:  DirectResponse
        @return: Success message
        """

    def addGraphDefinition(templateUid, graphDefinitionId, **kw):
        """
        Add a new graph definition to a template.

        @type  templateUid: string
        @param templateUid: Unique ID of the template to add graph definition to
        @type  graphDefinitionId: string
        @param graphDefinitionId: ID of the new graph definition

        @rtype:  DirectResponse
        @return: Success message
        """

    def deleteDataSource(uid, **kw):
        """
        Delete a data source.

        @type  uid: string
        @param uid: Unique ID of the data source to delete

        @rtype:  DirectResponse
        @return: Success message
        """

    def deleteDataPoint(uid, **kw):
        """
        Delete a data point.

        @type  uid: string
        @param uid: Unique ID of the data point to delete

        @rtype:  DirectResponse
        @return: Success message
        """

    def deleteGraphDefinition(uid, **kw):
        """
        Delete a graph definition.

        @type  uid: string
        @param uid: Unique ID of the graph definition to delete

        @rtype:  DirectResponse
        @return: Success message
        """

    def deleteGraphPoint(uid, **kw):
        """
        Delete a graph point.

        @type  uid: string
        @param uid: Unique ID of the graph point to delete

        @rtype:  DirectResponse
        @return: Success message
        """

    def getGraphPoints(uid, **kw):
        """
        Get a list of graph points for a graph definition.

        @type  uid: string
        @param uid: Unique ID of a graph definition

        @rtype:  DirectResponse
        @return: B{Properties}:
            - data: ([dictionary]) List of objects representing graph points
        """

    def getInfo(uid, **kw):
        """
        Get the properties of an object.

        @type  uid: string
        @param uid: Unique identifier of an object

        @rtype:   DirectResponse
        @return:  B{Properties}
            - data: (dictionary) Object properties
            - form: (dictionary) Object representing an ExtJS form for the object
        """

    def addThresholdToGraph(graphUid, thresholdUid, **kw):
        """
        Add a threshold to a graph definition.

        @type  graphUid: string
        @param graphUid: Unique ID of the graph definition to add threshold to
        @type  thresholdUid: string
        @param thresholdUid: Unique ID of the threshold to add

        @rtype:   DirectResponse
        @return:  Success message
        """

    def addCustomToGraph(graphUid, customId, customType, **kw):
        """
        Add a custom graph point to a graph definition.

        @type  graphUid: string
        @param graphUid: Unique ID of the graph definition to add graph point to
        @type  customId: string
        @param customId: ID of the new custom graph point
        @type  customType: string
        @param customType: Type of the new graph point. From getGraphInstructionTypes()

        @rtype:  DirectResponse
        @return: Success message
        """

    def getGraphInstructionTypes(query='', **kw):
        """
        Get a list of available instruction types for graph points.

        @type  query: string
        @param query: not used

        @rtype:   DirectResponse
        @return: B{Properties}:
            - data: ([dictionary]) List of objects representing instruction types
        """

    def setGraphPointSequence(uids, **kw):
        """
        Sets the sequence of graph points in a graph definition.

        @type  uids: [string]
        @param uids: List of graph point UID's in desired order

        @rtype:  DirectResponse
        @return: Success message
        """

    def getGraphDefinition(uid, **kw):
        """
        Get a graph definition.

        @type  uid: string
        @param uid: Unique ID of the graph definition to retrieve

        @rtype:   DirectResponse
        @return: B{Properties}:
            - data: (dictionary) Object representing a graph definition
        """

    def setGraphDefinition(**kw):
        """
        Set attributes on an graph definition.
        This method accepts any keyword argument for the property that you wish
        to set. Properties are enumerated via getGraphDefinition(). The only
        required property is "uid".

        @type    uid: string
        @keyword uid: Unique identifier of an object

        @rtype:  DirectResponse
        @return: B{Properties}:
            - data: (dictionary) The modified object
        """
        """
        Set a graph definition.
        """

    def setGraphDefinitionSequence(uids, **kw):
        """
        Sets the sequence of graph definitions.

        @type  uids: [string]
        @param uids: List of graph definition UID's in desired order

        @rtype:  DirectResponse
        @return: Success message
        """

