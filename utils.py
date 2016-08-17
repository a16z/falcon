#!/usr/bin/env python

import httplib2
import apiclient.discovery
import oauth2client.client
import os
import re
import time

def get_calendar_service(tokenFile):
    with open(tokenFile, 'r') as f:
        credentials = oauth2client.client.Credentials.new_from_json(f.read())
    http = httplib2.Http()
    credentials.authorize(http)
    return(apiclient.discovery.build('calendar', 'v3', http=http))

def getTimeZoneName():
    tzlink = os.readlink('/etc/localtime')
    pattern = '^/usr/share/zoneinfo/(.*)$'
    match = re.search(pattern, tzlink)
    return(match.group(1))

def getTimeZoneOffSet():
    if time.localtime().tm_isdst:
        tzoffset = time.altzone
    else:
        tzoffset = time.timezone
    hh = tzoffset / -3600
    mm = tzoffset % 60
    if hh < 0:
        sign = '-'
        hh *= -1
    else:
        sign = '+'
    return('{}{:02d}:{:02d}'.format(sign,hh,mm))
