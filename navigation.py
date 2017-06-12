import logging
import atexit
import time
from globals import *
import ev3dev.ev3 as ev3
from PIL import Image

LOGGER = logging.getLogger(__name__)


class ButtonAbort(BaseException):
    pass


def check_abort():
    if TOUCH_SENSOR.connected and TOUCH_SENSOR.value():
        raise ButtonAbort()


def abort_on_button(func):
    """ decorator to check_abort before/after running a function """

    def wrapper(*args, **kwargs):
        check_abort()
        retval = func(*args, **kwargs)
        check_abort()
        return retval

    return wrapper


@abort_on_button
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


@abort_on_button
def speak(words):
    """
    Speak the test in words

    :param words: str
    :return:
    """
    LOGGER.info("Saying: {}".format(words))
    if not SILENT:
        ev3.Sound.speak(words).wait()


@abort_on_button
def display_image(image, x=0, y=0):
        SCREEN.image.paste(Image.open(image), (x, y))
        SCREEN.update()


@abort_on_button
def sleep(seconds):
    """
    Sleep the specified seconds checking for abort button periodically

    :param seconds: float
    """
    end_time = time.time() + seconds
    while time.time() < end_time:
        time.sleep(.1)
        check_abort()


def wait_for_touch_sensor():
    """ wait for the touch sensor to be pressed """
    while True:
        if not TOUCH_SENSOR.connected:
            LOGGER.warning("Touch sensor not conneected")
            return
        if TOUCH_SENSOR.value():
            return
        time.sleep(.1)


@abort_on_button
def ir_distance():
    """
    Return the distance the IR sensor sees

    :return: float
    """
    # connect infrared and check it's connected.
    assert IR_SENSOR.connected, "Connect a single infrared sensor to port"

    # put the infrared sensor into proximity mode.
    IR_SENSOR.mode = 'IR-PROX'

    return IR_SENSOR.value()


def stop():
    """ stop all motors """
    LOGGER.debug("stopping")
    LEFT_MOTOR.stop()
    RIGHT_MOTOR.stop()


@abort_on_button
def start(speed=700):
    """
    Start the left/right motors at the specified speed

    :param speed: int, -1000 <-> 1000
    """
    LOGGER.debug("stopping")
    LEFT_MOTOR.run_forever(speed_sp=speed)
    RIGHT_MOTOR.run_forever(speed_sp=speed)


@abort_on_button
def turn(degrees):
    """
    Turns right or left the specified degrees, updates the global DIRECTION

    :param degrees: int, positive number turns right, negative turns left
    """
    global DIRECTION

    DIRECTION += degrees
    LEFT_MOTOR.run_rotations(ROTATIONS_PER_DEGREE * degrees)
    RIGHT_MOTOR.run_rotations(ROTATIONS_PER_DEGREE * degrees)


@abort_on_button
def turn_right():
    LOGGER.debug("turning right")
    stop()
    LEFT_MOTOR.run_to_rel_pos(position_sp=-305, speed_sp=360, stop_action="brake")
    RIGHT_MOTOR.run_to_rel_pos(position_sp=305, speed_sp=360, stop_action="brake")
    # TODO change to while not running / check_abort / sleep
    LEFT_MOTOR.wait_while('running')
    stop()


@abort_on_button
def turn_left():
    LOGGER.debug("turning left")
    stop()
    LEFT_MOTOR.run_to_rel_pos(position_sp=305, speed_sp=360, stop_action="brake")
    RIGHT_MOTOR.run_to_rel_pos(position_sp=-305, speed_sp=360, stop_action="brake")
    # TODO change to while not running / check_abort / sleep
    LEFT_MOTOR.wait_while('running')
    stop()


@abort_on_button
def move(centimeters: float, speed: int = 700, stop_action: str = "brake") -> None:
    """
    Move the specified centimeters and wait for the motor to stop

    :param centimeters: float
    :param speed: int
    :param stop_action: str
    :rtype: float
    """
    rotations = centimeters / WHEEL_CIRCUMFERENCE * 360
    LOGGER.debug("Running %d rotations at %d then %s", rotations, speed, stop_action)
    LEFT_MOTOR.run_to_rel_pos(position_sp=rotations, speed_sp=int(speed * .993), stop_action=stop_action)
    RIGHT_MOTOR.run_to_rel_pos(position_sp=rotations, speed_sp=speed, stop_action=stop_action)
    # TODO change to while not running / check_abort / sleep
    LEFT_MOTOR.wait_while('running')


@abort_on_button
def smart_move(centimeters):
    """
    move specified centimeters avoiding things along the way

    returns number of centimeters turned to avoid (+/- for right/left)

    :param centimeters: int, how far to move
    :return: int
    """
    moved_right = 0
    remaining = centimeters
    start_pos = moved()
    start()
    # Run until we've gone how far we want to go or until we hit something
    while remaining > 0:
        check_abort()
        LOGGER.debug("Remaining %s", remaining)
        if ir_distance() < 20:
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


@abort_on_button
def moved():
    """
    returns centimeters moved since last reset

    :return: int
    """
    return LEFT_MOTOR.position / 360 * WHEEL_CIRCUMFERENCE


atexit.register(stop)
