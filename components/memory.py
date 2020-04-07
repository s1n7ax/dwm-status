#!/bin/python

from subprocess import Popen,PIPE
from dwm_status_events import trigger_change_event
from shell_exe import execute
from threading import Timer, Thread

class Memory:
    def __init__(self):
        self.details = '💻 MEM 0.00Gi/0.00Gi'
        Thread(self.set_details()).start()

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
        self.details = self.get_details()
        Timer(5, self.set_details).start()

    def __str__(self):
        return self.details
