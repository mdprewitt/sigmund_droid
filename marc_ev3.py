#!/usr/bin/env python3
from ev3dev.ev3 import *
from globals import *
from navigation import *

FEET_PER_SECOND = 4


def msecs_for_feet(feet):
    return int(feet * FEET_PER_SECOND * 1000)


def wait(motor):
    while 'running' in motor.command:
        pass


def main():
    Sound.speak('Here we go!').wait()

    motor_max_speed = LEFT_MOTOR.max_speed
    speed = 80

    # full steam ahead!
    LEFT_MOTOR.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(3))
    RIGHT_MOTOR.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(3))

    wait(LEFT_MOTOR)

    # turn right
    LEFT_MOTOR.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(.5))
    RIGHT_MOTOR.run_timed(speed_sp=-motor_max_speed * speed, time_sp=msecs_for_feet(.5))

    wait(LEFT_MOTOR)

    # resume speed
    LEFT_MOTOR.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(2))
    RIGHT_MOTOR.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(2))

    wait(LEFT_MOTOR)

if __name__ == '__main__':
    main()
