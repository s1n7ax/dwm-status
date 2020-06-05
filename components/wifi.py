#!/bin/python

from dwm_status_events import trigger_change_event, on_signal
from shell_exe import execute
from threading import Thread
from subprocess import CalledProcessError

class Wifi:
    def __init__(self):
        self.ssid='🖧 '
        Thread(self.set_details()).start()

    def get_details(self):
        try:
            ssid = execute([["iwgetid", "-r"]])
        except CalledProcessError:
            ssid = 'not connected'
        
        return "🖧  {}".format(ssid)

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.ssid = self.get_details()

    def __str__(self):
        return self.ssid
