#!/usr/bin/env python3
from ev3dev.ev3 import *
from globals import *
from navigation import *

# Connect infrared sensor to any sensor port
# and check it is connected.
ir = InfraredSensor() 
assert ir.connected, "Connect an IR sensor to any sensor port"

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

FEET_PER_SECOND = 4

def msecs_for_feet(feet):
    return int(feet * FEET_PER_SECOND * 1000)


def wait(motor):
#    while 'running' in motor.command:
     motor.wait_while('running')

def main():
    Sound.speak('Here we go!').wait()

    motor_max_speed = LEFT_MOTOR.max_speed
    motor_half_speed = LEFT_MOTOR.max_speed/2
    speed = 80

    # full steam ahead!
    LEFT_MOTOR.run_timed(speed_sp=-motor_max_speed, time_sp=msecs_for_feet(.5))
    RIGHT_MOTOR.run_timed(speed_sp=-motor_max_speed, time_sp=msecs_for_feet(.5))

    wait(LEFT_MOTOR)

    # turn right
    #LEFT_MOTOR.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(.5))
    #RIGHT_MOTOR.run_timed(speed_sp=-motor_max_speed * speed, time_sp=msecs_for_feet(.5))
    LEFT_MOTOR.run_timed(speed_sp=motor_half_speed, time_sp=msecs_for_feet(.16))
    RIGHT_MOTOR.run_timed(speed_sp=-motor_half_speed, time_sp=msecs_for_feet(.16))

    wait(LEFT_MOTOR)

    # resume speed
    LEFT_MOTOR.run_timed(speed_sp=-motor_max_speed, time_sp=msecs_for_feet(.5))
    RIGHT_MOTOR.run_timed(speed_sp=-motor_max_speed, time_sp=msecs_for_feet(.5))

    wait(LEFT_MOTOR)

if __name__ == '__main__':
    main()
