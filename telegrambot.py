#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from configparser import ConfigParser

import logging
import re
import random

import RPi.GPIO as GPIO 

cfg = ConfigParser()
cfg.read('bot.cfg')

DOOR_PIN = 23
DOOR_OPEN_MSG   = 'Ovi on auki.'
DOOR_CLOSED_MSG = 'Ovi on kiinni.'

def setupDoorMonitor():
    # Set GPIO mode to BCM (https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)
    GPIO.setmode(GPIO.BCM)

    # Set pin as input and use pull-up (open = true, closed = false)
    GPIO.setup(DOOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getDoorStateMessage():
    return DOOR_OPEN_MSG if GPIO.input(DOOR_PIN) else DOOR_CLOSED_MSG

def ovi(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=getDoorStateMessage())

def skiltaa(bot, update):
    msg = update.message
    if msg.text is not None:
        if 'skiltua' in msg.text.lower():
            bot.sendMessage(chat_id=update.message.chat_id, text="skiltua")

def main():
    setupDoorMonitor()

    updater = Updater(cfg['TELEGRAM']['token'])
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    ovire = re.compile(r'^/ovi$', flags=re.IGNORECASE)
    ovi_handler = RegexHandler(ovire, ovi)
    dispatcher.add_handler(ovi_handler)

    skiltu_handler = MessageHandler(Filters.all, skiltaa)
    dispatcher.add_handler(skiltu_handler)

    updater.start_polling()
    updater.idle()

main()
