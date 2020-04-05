#!/bin/python
from dwm_status_events import trigger_change_event
import urllib.request
import threading

class Weather:
    def __init__(self, location):
        self.url = 'http://wttr.in/{}?format=1'.format(location)
        self.weather= 'loading'
        t1 = threading.Thread(target=self.setDetails, args=[])
        t1.start()

    def getDetails(self):
        try:
            return urllib.request.urlopen(self.url).read().decode('utf-8')
        except:
            return ''


    @trigger_change_event
    def setDetails(self):
        self.weather = self.getDetails()
        return threading.Timer(1 * 60 * 60, self.setDetails).start()

    def __str__(self):
        return self.weather
