#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from PIL import Image
import ev3dev.ev3 as ev3

from globals import *
from navigation import *

def speak(words):
    ev3.Sound.speak(words).wait()

# connect infrared and check it's connected.
ir = InfraredSensor()
assert ir.connected, "Connect a single infrared sensor to port"

# put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

# Record the initial separation of the sensor and the object
startdistance = ir.value()

# add condition here
# while

distance = ir.value()

if distance < 500:
    Leds.set_color(Leds.LEFT, Leds.GREEN)
    lcd = Screen()
    logo = Image.open('chase.png')
    lcd.image.paste(logo, (0, 0))
    lcd.update()

    speak('Welcome to JP Morgan Chase. Who are you looking for?')

else:
    Leds.all_off()
    sleep(2)

# create motor objects
LEFT_MOTOR = LargeMotor('outB')
RIGHT_MOTOR = LargeMotor('outC')

start = LEFT_MOTOR.position_sp
move(75)
# Run until we've gone how far we want to go or until we hit something
done = False
while not done:
    distance = ir.value()
    print(LEFT_MOTOR.position_sp)
    if 'running' not in LEFT_MOTOR.state:
        done = True
        print("reached distance")
    elif distance < 20:
        print("ran into something")
        stop()
        # speak("Pardon me")
        turn_right()
        move(15)
        turn_left()
    else:
        sleep(0.01)

exit(0)
turn_right()

# go straight 2 feet (in degrees)
LEFT_MOTOR.wait_while('running')
RIGHT_MOTOR.wait_while('running')
LEFT_MOTOR.run_to_rel_pos(position_sp=1247.4109711133922, speed_sp=900, stop_action="brake")
RIGHT_MOTOR.run_to_rel_pos(position_sp=1247.4109711133922, speed_sp=900, stop_action="brake")
