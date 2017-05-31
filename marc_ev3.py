#!/usr/bin/env python3
from ev3dev.ev3 import *

FEET_PER_SECOND = 4


def msecs_for_feet(feet):
    return int(feet * FEET_PER_SECOND * 1000)


def wait(motor):
    while 'running' in motor.command:
        pass


def main():
    Sound.speak('Here we go!').wait()

    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_B)
    motor_max_speed = left_motor.max_speed
    speed = 80

    # full steam ahead!
    left_motor.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(3))
    right_motor.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(3))

    wait(left_motor)

    # turn right
    left_motor.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(.5))
    right_motor.run_timed(speed_sp=-motor_max_speed * speed, time_sp=msecs_for_feet(.5))

    wait(left_motor)

    # resume speed
    left_motor.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(2))
    right_motor.run_timed(speed_sp=motor_max_speed * speed, time_sp=msecs_for_feet(2))

    wait(left_motor)

if __name__ == '__main__':
    main()
