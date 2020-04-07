#!/bin/python
import time
import subprocess
import signal
from dwm_status_events import add_changed_event_listener, on_signal_callbacks
from components.weather import Weather
from components.cpu import CPU
from components.memory import Memory
from components.storage import Storage 
from components.volume import Volume 
from components.datetime import DateTime 
from components.wifi import Wifi 


#------------------------------------------------------------------------------#
#                               STATUS COMPONENTS                              #
#------------------------------------------------------------------------------#
status_list = [ 
    Weather("Colombo"), 
    CPU(),
    Memory(),
    Storage(),
    DateTime(),
    Volume(),
    Wifi(), #WIP
]

sep = ' | '

'''
updates the status bar
'''
def update_status():
    name = ''
    for stat in status_list:
        value = str(stat)

        if value == '':
            continue

        name = name + sep + str(stat)

    name = name + sep

    subprocess.run(["xsetroot", "-name", name])


'''
on value change callback function
'''
def on_change():
    update_status()

def on_signal(_x, _y):
    for callback in on_signal_callbacks:
        print('on signal before')
        callback()
        print('on signal after')


'''
main
'''
def __main__():
    # register on change 
    add_changed_event_listener(on_change)

    # register on signal
    signal.signal(signal.SIGUSR1, on_signal)

    # setting init status
    update_status()


__main__()
