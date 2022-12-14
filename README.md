# door-telegram-bot

Simple script to monitor door state with magnetic switch, and poll the state through telegram bot API. Can also be used to monitor other things which can connect to Raspberry Pi GPIO inputs.

doormonitor.py is a script which can be used to write the state to a file for further purposes.

Uses python3 and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). Designed to run on an Raspberry Pi, but can be used with other devices as well with proper modifications.

Currently in use at Sähkökilta guild room in Tampere.
