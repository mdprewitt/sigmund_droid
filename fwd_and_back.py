#!/usr/bin/env python3
# The robot will move forward in a straight line (speed=50%) until it has moved (at least) 31 cm closer to the reflecting object in front of it, then it will stop and pause for one second, then it will back up continuously (speed=-50%) until it detects that it has moved within 1 cm of it's starting position, then it will stop.

from ev3dev.ev3 import *

from time import sleep

# Connect ultrasonic sensor and check connected.
us = UltrasonicSensor()
assert us.connected, "Connect ultrasonic sensor to any sensor port"

# Put the US sensor into distance mode.
us.mode='US-DIST-CM'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

# Record the initial separation of the sensor and the object
startdistance = us.value()

# Advance at 50% speed (speed_sp=450)
mB.run_forever(speed_sp=450)
mC.run_forever(speed_sp=450)

# Wait until robot has moved (at least) 31 cm (310 mm) closer
# to the reflecting object in front of it
while us.value() > startdistance-310:
    sleep(0.01)

# Turn off the motors and apply the brake
mB.stop(stop_action="brake")
mC.stop(stop_action="brake")
sleep(1)

# Reverse at 50% speed
mB.run_forever(speed_sp=-450)
mC.run_forever(speed_sp=-450)

# Wait until robot is less than 1 cm from its starting position
while us.value() < startdistance-10:
    sleep(0.01)

mB.stop()
mC.stop()