# Update door status in file door_status.txt based on magnetic switch state.

import time 
import RPi.GPIO as GPIO 
import logging

def writeState(state):
		f = open('door_status.txt', 'w')
		f.write(state)
		f.close()

def setup():
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='ovi.log', level=logging.INFO)

	# Set GPIO mode to BCM (https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)
	GPIO.setmode(io.BCM)

	DOOR_PIN = 23

	# Set pin as input and use pull-up (open = true, closed = false)
	GPIO.setup(DOOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	currentState = GPIO.input(DOOR_PIN)
	previousState = currentState

	# Write initial state
	writeState(currentState)
	
	# Initialize door to start logging when script starts
	#initialState = 'Door is open.' if doorOpen else 'Door is closed'
	#logging.info('Script started!')
	#logging.info(initialState)

def main():
	setup()

	while True:
		currentState = GPIO.input(DOOR_PIN)

		if (currentState != previousState):
			doorStatus = 'open' if currentState else '0'
			writeState(currentState)
			previousState = currentState
		
		time.sleep(5)

main()
