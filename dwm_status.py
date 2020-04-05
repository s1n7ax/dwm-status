#!/bin/python
from dwm_status_events import add_changed_event_listener, on_signal_callbacks
from components.weather import Weather
from components.cpu import CPU
from components.memory import Memory
from components.storage import Storage 
from components.volume import Volume 
import time
import subprocess
import signal


#------------------------------------------------------------------------------#
#                               STATUS COMPONENTS                              #
#------------------------------------------------------------------------------#
status_list = [ 
    Weather("Colombo"), 
    CPU(),
    Memory(),
    Storage(),
    Volume()
]

sep = ' | '

'''
update the status bar
'''
def update_status():
    name = ''
    for stat in status_list:
        value = str(stat)

        if value == '':
            continue

        name = name + sep + str(stat)

    subprocess.run(["xsetroot", "-name", name])


'''
on value change callback function
'''
def on_change():
    update_status()

'''
main
'''
def __main__():
    add_changed_event_listener(on_change)

    for callback in on_signal_callbacks:
        signal.signal(signal.SIGUSR1, lambda x, y: (callback()))

    # setting init status
    update_status()


__main__()
