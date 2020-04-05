#!/bin/python
from subprocess import Popen,PIPE
from dwm_status_events import trigger_change_event, on_signal
from shell_exe import execute
import threading

class Volume:
    def __init__(self):
        self.set_details()

    def get_details(self):
        volume = execute([
            ["amixer", "sget", "Master"],
            ["tail", "-n1"],
            ["sed", "-r", "s/.*\\[(.*)%\\].*/\\1/"]
        ]).replace('\n', '')
        return "VOL {}%".format(volume)

    @on_signal
    @trigger_change_event
    def set_details(self):
        self.resources = self.get_details()

    def __str__(self):
        return self.resources



