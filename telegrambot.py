#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters

import logging
import re

import RPi.GPIO as GPIO 

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

def ovi(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=getDoorStateMessage())

def main():
    setupDoorMonitor()

    updater = Updater("YOUR_TOKEN_HERE", use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    ovire = re.compile(r'^/ovi$', flags=re.IGNORECASE)
    ovi_handler = MessageHandler(Filters.regex(ovire), ovi)
    dispatcher.add_handler(ovi_handler)

    updater.start_polling()
    updater.idle()

main()
