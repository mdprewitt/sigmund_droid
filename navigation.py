from time import sleep
import logging
import atexit
from globals import *
import ev3dev.ev3 as ev3

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
    LEFT_MOTOR.reset()
    RIGHT_MOTOR.reset()
    # motor_polarity = 'normal' if motor_normal_polarity else 'inversed'
    # LEFT_MOTOR.polarity(motor_polarity)
    # RIGHT_MOTOR.polarity(motor_polarity)
    # MEDIUM_MOTOR.polarity(motor_polarity)
    global DIRECTION
    global X_POSITION
    global Y_POSITION
    DIRECTION = direction
    X_POSITION = x_position
    Y_POSITION = y_position


def speak(words):
    LOGGER.info("Saying: {}".format(words))
    if not SILENT:
        ev3.Sound.speak(words).wait()


def stop():
    LOGGER.debug("stopping")
    LEFT_MOTOR.stop()
    RIGHT_MOTOR.stop()
    

def start():
    LOGGER.debug("stopping")
    LEFT_MOTOR.run_forever(speed_sp=360)
    RIGHT_MOTOR.run_forever(speed_sp=360)
    

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
    LOGGER.debug("turning right")
    stop()
    LEFT_MOTOR.run_to_rel_pos(position_sp=-305, speed_sp=360, stop_action="brake")
    RIGHT_MOTOR.run_to_rel_pos(position_sp=305, speed_sp=360, stop_action="brake")
    LEFT_MOTOR.wait_while('running')
    stop()


def turn_left():
    LOGGER.debug("turning left")
    stop()
    LEFT_MOTOR.run_to_rel_pos(position_sp=305, speed_sp=360, stop_action="brake")
    RIGHT_MOTOR.run_to_rel_pos(position_sp=-305, speed_sp=360, stop_action="brake")
    LEFT_MOTOR.wait_while('running')
    stop()


def smart_move(centimeters):
    """
    move specified centimeters avoiding things along the way

    returns number of centimeters turned to avoid (+/- for right/left)
    """
    ir = ev3.InfraredSensor()
    assert ir.connected, "Connect a single infrared sensor to port"
    moved_right = 0
    remaining = centimeters
    start_pos = moved()
    start()
    # Run until we've gone how far we want to go or until we hit something
    done = False
    while remaining > 0:
        LOGGER.debug("Remaining %s", remaining)
        if ir.value() < 20:
            LOGGER.info("ran into something at %s", moved())
            stop()
            speak("Pardon me")
            turn_right()
            move(15)
            moved_right += 15
            turn_left()
            start_pos = moved()
            start()
        sleep(0.01)
        remaining -= moved() - start_pos
        start_pos = moved()
    return moved_right


def move(centimeters, speed=700, stop_action="brake"):
    rotations = centimeters / WHEEL_CIRCUMFERENCE * 360
    LOGGER.debug("Running %d rotations at %d then %s", rotations, speed, stop_action)
    LEFT_MOTOR.run_to_rel_pos(position_sp=rotations, speed_sp=int(speed*.993), stop_action=stop_action)
    RIGHT_MOTOR.run_to_rel_pos(position_sp=rotations, speed_sp=speed, stop_action=stop_action)
    LEFT_MOTOR.wait_while('running')

def moved():
    """ returns centimeters moved since last reset """
    return LEFT_MOTOR.position / 360 * WHEEL_CIRCUMFERENCE

def move_north(centimeters):
    global X_POSITION
    global Y_POSITION
    X_POSITION += centimeters
    rotations = centimeters / WHEEL_CIRCUMFERENCE * 360
    LEFT_MOTOR.run_rotations(centimeters)
    RIGHT_MOTOR.run_rotations(centimeters)

atexit.register(stop)
