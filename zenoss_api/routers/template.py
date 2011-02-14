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
Template router for the Zenoss JSON API
"""

from zope.interface import implements

from zenoss_api.interfaces import ITemplate
from zenoss_api.router import RouterBase
from zenoss_api.utils import myArgs

info = {"name": "template",
    "author": "Endre Karlson endre.karlson@gmail.com",
    "version": "0.1",
    "class": "Template"}


class Template(RouterBase):
    implements(ITemplate)

    # Location + action
    location = 'template_router'
    action = 'TemplateRouter'

    def getTemplates(self, id, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDeviceClassTemplates(self, id, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getAddTemplateTargets(self, query, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addTemplate(self, id, targetUid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteTemplate(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getThresholds(self, uid, query='', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getThresholdDetails(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDataPoints(self, query, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addDataPoint(self, dataSourceUid, name, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addDataSource(self, templateUid, name, type, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDataSources(self, id, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDataSourceDetails(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDataPointDetails(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setInfo(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addThreshold(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def removeThreshold(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getThresholdTypes(self, query, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getDataSourceTypes(self, query, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getGraphs(self, uid, query=None):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addDataPointToGraph(self, dataPointUid, graphUid,
                            includeThresholds=False, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getCopyTargets(self, uid, query='', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def copyTemplate(self, uid, targetUid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addGraphDefinition(self, templateUid, graphDefinitionId, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteDataSource(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteDataPoint(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteGraphDefinition(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def deleteGraphPoint(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getGraphPoints(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getInfo(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addThresholdToGraph(self, graphUid, thresholdUid, **Kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def addCustomToGraph(self, graphUid, customId, customType, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getGraphInstructionTypes(self, query='', **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setGraphPointSequence(self, uids, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def getGraphDefinition(self, uid, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setGraphDefinition(self, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)

    def setGraphDefinitionSequence(self, uids, **kw):
        args = myArgs()[0]
        return self._request(args, **kw)
