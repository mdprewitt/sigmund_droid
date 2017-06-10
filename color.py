#!/usr/bin/env python3

from ev3dev.ev3 import *
import sigmund_demo

locations = {'green': (1,3), 'blue': (5, 3), 'yellow': (1, 1), 'brown': (1, 5)}

cl = ColorSensor()
assert cl.connected

cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')

while cl.value() == 5:
    if cl.value() == 2:
        Leds.set_color(Leds.RIGHT, (Leds.AMBER))
