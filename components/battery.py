#!/bin/python

from subprocess import Popen,PIPE
from dwm_status_events import trigger_change_event
from shell_exe import execute
from threading import Timer, Thread
import subprocess

class Battery:
    def __init__(self):
        self.details = ' 00.00%'
        Thread(self.set_details()).start()

    def get_details(self):
        bat = subprocess.check_output("cat /sys/class/power_supply/BAT0/capacity",shell=True)
        return "BAT "+str(float(bat))+"%"

    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(2, self.set_details).start()

    def __str__(self):
        return self.details
