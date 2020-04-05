#!/bin/python
from subprocess import Popen,PIPE
from dwm_status_events import trigger_change_event
from shell_exe import execute
import threading

class Memory:
    def __init__(self):
        self.set_details()

    def get_details(self):
        mem_used = execute([
            ["free", "-h"],
            ["awk", '(NR == 2) {print $3}']
        ]).replace('\n', '')

        mem_tot = execute([
            ["free", "-h"],
            ["awk", '(NR == 2) {print $2}']
        ]).replace('\n', '')

        return "💻 MEM {}/{}".format(mem_used, mem_tot)

    @trigger_change_event
    def set_details(self):
        self.resources = self.get_details()
        threading.Timer(5 * 60, self.set_details).start()

    def __str__(self):
        return self.resources



