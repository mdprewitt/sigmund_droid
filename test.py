#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from PIL import Image
import ev3dev.ev3 as ev3



#connect infrared and check it's connected.
ir = InfraredSensor()
assert ir.connected, "Connect a single infrared sensor to port"

#put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

#add condition here
#while
  
distance = ir.value()

if distance < 500:
 Leds.set_color(Leds.LEFT, Leds.GREEN)
 lcd = Screen()
 logo = Image.open('chase.png')
 lcd.image.paste(logo, (0,0))
 lcd.update()
 ev3.Sound.speak('Welcome to JP Morgan Chase, who are you looking for?').wait()

else:
 Leds.all_off()
 sleep(2)


#create motor objects
lm = LargeMotor('outB')
rm = LargeMotor ('outC')

#go straight for 3 feet (in degrees)
lm.run_to_rel_pos(position_sp=-1871.1164566700884, speed_sp=900, stop_action="brake")
rm.run_to_rel_pos(position_sp=-1871.1164566700884, speed_sp=900, stop_action="brake")
lm.wait_while('running')
rm.wait_while('running')

#verify the motor is no longer running
#Sound.beep()

#turn right
lm.run_to_rel_pos(position_sp=300, speed_sp=360, stop_action="brake")
rm.run_to_rel_pos(position_sp=-300, speed_sp=360, stop_action="brake")


#go straight 2 feet (in degrees)
lm.wait_while('running')
rm.wait_while('running')
lm.run_to_rel_pos(position_sp=-1247.4109711133922, speed_sp=900, stop_action="brake")
rm.run_to_rel_pos(position_sp=-1247.4109711133922, speed_sp=900, stop_action="brake")

