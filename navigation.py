from globals import *
import logging
LOGGER = logging.getLogger(__name__)


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


def stop():
    LEFT_MOTOR.stop()
    RIGHT_MOTOR.stop()
    

def turn(degrees):
    """
    @param degrees: int, positive number turns right, negative turns left
    Turns right or left the specified degrees, updates the global DIRECTION
    """
    global DIRECTION

    DIRECTION += degrees
    LEFT_MOTOR.run_rotations(ROTATIONS_PER_DEGREE * degrees)
    RIGHT_MOTOR.run_rotations(ROTATIONS_PER_DEGREE * degrees)


def turn_right():
    LEFT_MOTOR.run_to_rel_pos(position_sp=305, speed_sp=360, stop_action="brake")
    RIGHT_MOTOR.run_to_rel_pos(position_sp=-305, speed_sp=360, stop_action="brake")


def turn_left():
    LEFT_MOTOR.run_to_rel_pos(position_sp=-305, speed_sp=360, stop_action="brake")
    RIGHT_MOTOR.run_to_rel_pos(position_sp=305, speed_sp=360, stop_action="brake")


def move(centimeters, speed=700, stop_action="brake"):
    rotations = centimeters / WHEEL_CIRCUMFERENCE * 360
    LOGGER.debug("Running %d rotations at %d then %s", rotations, speed, stop_action)
    LEFT_MOTOR.run_to_rel_pos(position_sp=rotations, speed_sp=int(speed*.993), stop_action=stop_action)
    RIGHT_MOTOR.run_to_rel_pos(position_sp=rotations, speed_sp=speed, stop_action=stop_action)


def move_north(centimeters):
    global X_POSITION
    global Y_POSITION
    X_POSITION += centimeters
    rotations = centimeters / WHEEL_CIRCUMFERENCE * 360
    LEFT_MOTOR.run_rotations(centimeters)
    RIGHT_MOTOR.run_rotations(centimeters)
