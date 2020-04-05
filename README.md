# dwm-status
`dwm-status` is a simple python program for setting `dwm status bar`. One special thing about `dwm-status` is, it loads or reads resources only when needed. If I'm reading `CPU` usage in every second it doesn't mean I have to read or load all the other resources (storage for example) each and every second right? So every `dwm-status-component` reads/load details independently from others.


### Requirements
Install following packages:
```
python3 (dwm-status is a python3 program)
lm_sensors (for reading CPU details)
amixer (for reading volume)
```

Internet connection: this is required to get the weather details (weather details are removed from the status bar when failed to get details)

## Weather Location Details:
This uses `http://wttr.in/<location>` endpoint to get weather details. So the location passed to `Weather` constructor will be replace `<location>` in the URL.

#### dwm_status.py
```python
status_list = [ 
    Weather("Colombo"), 
]
```

## Volume Controls:
`Volume` component is listening to `SIGUSR1` custom signal and triggers `set_details()` method. Because it's using `@trigger_change_event` decorator, call to this method will trigger `update_status()`

```python
@on_signal
@trigger_change_event
def setDetails(self):
	self.resources = self.getDetails()
```

So if you run `kill -SIGUSR1 $(pgrep dwm_status.py)` in a terminal window will trigger `@on_signal` methods. So I automated this process using `sxhkd` as follows

#### .config/sxhkd/sxhkdrc
```bash
#------------------------------------------------------------------------------#
#                              independent hotkeys                             #
#------------------------------------------------------------------------------#
# make sxhkd reload its configuration files:
alt + Escape
	pkill -USR1 -x sxhkd

# runs when increase/decrease volume function keys are pressed
XF86Audio{Raise,Lower}Volume
    pactl set-sink-volume @DEFAULT_SINK@ {+10%,-10%} && kill -SIGUSR1 $(pgrep dwm_status.py)
```
