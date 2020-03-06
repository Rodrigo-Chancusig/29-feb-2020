# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:35:04 2020

@author: CEC
"""

from gpiozero import LED
from time import sleep

led = LED(18)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)