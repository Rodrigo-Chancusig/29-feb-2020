# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:36:52 2020

@author: CEC
"""

from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(3)

button.when_pressed = led.on
button.when_released = led.off

pause()