#!/bin/python
from subprocess import Popen,PIPE
from dwm_status_events import trigger_change_event, on_signal
from shell_exe import execute
import threading

class Volume:
    def __init__(self):
        self.setDetails()

    def getDetails(self):
        volume = execute([
            ["amixer", "sget", "Master"],
            ["tail", "-n1"],
            ["sed", "-r", "s/.*\\[(.*)%\\].*/\\1/"]
        ]).replace('\n', '')
        return "VOL {}%".format(volume)

    @on_signal
    @trigger_change_event
    def setDetails(self):
        self.resources = self.getDetails()

    def __str__(self):
        return self.resources



