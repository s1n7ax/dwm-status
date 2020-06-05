#!/bin/python
from functools import partial
import signal

on_chage_callbacks = []
on_signal_callbacks = set([])


def add_changed_event_listener(callback):
    on_chage_callbacks.append(callback)


'''
runs on_chage_callbacks on event
'''


def trigger_change_event(org_func):
    def wrapper(self):
        org_func(self)
        for callback in on_chage_callbacks:
            callback()

    return wrapper


'''
register status component functions to SIGUSR1 event
'''


def on_signal(callback):
    def wrapper(self):
        on_signal_callbacks.add(partial(callback, self))
        callback(self)
    return wrapper
