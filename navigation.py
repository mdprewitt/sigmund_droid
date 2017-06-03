from globals import *


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
