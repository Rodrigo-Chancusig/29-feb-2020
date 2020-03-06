# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:21:45 2020

@author: CEC
"""

import RPi.GPIO as GPIO
import time 

GPIO.setwarning(False) # desactiva las alertas 
GPIO.setmode(GPIO.BCM) # forma de controlar los pines de la rpi
GPIO.setup(18,GPIO.OUT) # pin que se usa de salida 
GPIO.setup(25, GPIO.IN)

while True:
    if GPIO.input(25):
        GPIO.output(18, False)
    else:
        GPIO.output(18, True)
