#!/bin/python
from dwm_status_events import trigger_change_event
import urllib.request
import threading
import time

class Weather:
    def __init__(self, location):
        self.url = 'http://wttr.in/{}?format=1'.format(location)
        self.weather= 'loading'
        t1 = threading.Thread(target=self.set_details, args=[])
        t1.start()

    def get_details(self):
        for x in range(0, 10):
            try:
                return urllib.request.urlopen(self.url).read().decode('utf-8')
            except:
                time.sleep(1)
        return ''


    @trigger_change_event
    def set_details(self):
        self.weather = self.get_details()
        return threading.Timer(60 * 60, self.set_details).start()

    def __str__(self):
        return self.weather
