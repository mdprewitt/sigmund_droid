from globals import *


def initialize(direction=0, x_position=0, y_position=0, motor_normal_polarity=True):
    """
    Setup the robot defaults/location/etc...

    :param direction: int, 0 by default
    :param x_position: int, 0 by default
    :param y_position: int, 0 by default
    :param motor_normal_polarity: bool, True for 'normal polarity, otherwise motors are 'inversed'

    :return:
    """
    motor_polarity = 'normal' if motor_normal_polarity else 'inversed'
    LEFT_MOTOR.polarity(motor_polarity)
    RIGHT_MOTOR.polarity(motor_polarity)
    MEDIUM_MOTOR.polarity(motor_polarity)
    global DIRECTION
    global X_POSITION
    global Y_POSITION
    DIRECTION = direction
    X_POSITION = x_position
    Y_POSITION = y_position


def turn(degrees):
    """
    @param degrees: int, positive number turns right, negative turns left

    Turns right or left the specified degrees, updates the global DIRECTION
    """
    global DIRECTION

    DIRECTION += degrees
    LEFT_MOTOR.run_rotations(ROTATIONS_PER_DEGREE * degrees)
    LEFT_MOTOR.run_rotations(ROTATIONS_PER_DEGREE * degrees)


def move_north(centimeters):
    global X_POSITION
    global Y_POSITION
    X_POSITION += centimeters
    LEFT_MOTOR.run_rotations(ROTATIONS_PER_CM * centimeters)
    LEFT_MOTOR.run_rotations(ROTATIONS_PER_CM * centimeters)
