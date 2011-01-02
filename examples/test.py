#!/usr/bin/env python

import zenoss_api

api = zenoss_api.ZenossAPI()

print api.get_devices()
