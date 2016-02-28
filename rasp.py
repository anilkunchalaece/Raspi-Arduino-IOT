
import RPi.GPIO as GPIO
import time
import sys
import serial
from pubnub import Pubnub

ser = serial.Serial('/dev/ttyACM1',9600)

GPIO.setmode (GPIO.BCM)

LED_PIN = 4

GPIO.setup(LED_PIN,GPIO.OUT)


pubnub = Pubnub(publish_key='pub-c-9e022950-208f-49aa-9873-c560add30b41', subscribe_key='sub-c-9ddf7ad2-cfec-11e5-b522-0619f8945a4f')

channel = 'anil'

def _callback(m, channel):
	print(m)
	ser.write(m['led'])

def _error(m):
	print(m)
 
pubnub.subscribe(channels=channel, callback=_callback, error=_error)
