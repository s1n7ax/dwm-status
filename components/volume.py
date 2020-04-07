#!/bin/python

from subprocess import Popen,PIPE
from dwm_status_events import trigger_change_event, on_signal
from shell_exe import execute
from threading import Timer, Thread

class Volume:
    def __init__(self):
        self.details = '🔉 {:.>3s}%'.format('0')
        Thread(self.set_details()).start()

    def get_details(self):
        details = execute([
            ["amixer", "sget", "Master"],
            ["tail", "-n1"],
            ["sed", "-r", "s/.*\\[(.*)%\\].*/\\1/"]
        ]).replace('\n', '')
        return "🔉 {:>3s}%".format(details)

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()

    def __str__(self):
        return self.details
