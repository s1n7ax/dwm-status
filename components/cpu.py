#!/bin/python

from subprocess import Popen,PIPE
from dwm_status_events import trigger_change_event
from shell_exe import execute
from threading import Timer, Thread

class CPU:
    def __init__(self):
        self.details = 'CPU 00.00%'
        Thread(self.set_details()).start()

    def get_details(self):
        cpu = execute([
            ["sensors"],
            ["grep", "^Core.*"],
            ["awk", '{ gensub(/\\+(\\\\d)°C/, "\\\\1", "g", $3) } {s+=$3} END {print s/NR}']
        ]).replace('\n', '')

        return "CPU {:.2f}%".format(float(cpu))

    @trigger_change_event
    def set_details(self):
        self.details = self.get_details()
        Timer(2, self.set_details).start()

    def __str__(self):
        return self.details
