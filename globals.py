from math import pi
from ev3dev.ev3 import (
    LargeMotor,
    OUTPUT_C,
    OUTPUT_B,
    OUTPUT_A,
    MediumMotor,
    TouchSensor,
    InfraredSensor,
    Screen,
    Leds,
)


X_POSITION = 0
Y_POSITION = 0

RED_DESK = tuple([30, 20])
BLUE_DESK = tuple([30, -20])

WHEEL_DIAMETER = 4.3  # centimeters
WHEEL_CIRCUMFERENCE = pi * WHEEL_DIAMETER
ROTATIONS_PER_CM = 360 * WHEEL_CIRCUMFERENCE
# TODO ROTATIONS_PER_DEGREE needs a real number, .5 is just a wild guess
ROTATIONS_PER_DEGREE = .5  # how many rotations to turn specified degrees
"""
           0
           |
-90/270 ---|--- 90/-270
           |
       180/-180
"""
DIRECTION = 0 

LEFT_MOTOR = LargeMotor(OUTPUT_B)
RIGHT_MOTOR = LargeMotor(OUTPUT_C)
MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
TOUCH_SENSOR = TouchSensor()
IR_SENSOR = InfraredSensor()
SCREEN = Screen()
LEDS = Leds

SILENT = False
SP_FOR_90_DEG_TURN = 295


def set_silent(silent=False):
    global SILENT
    SILENT = silent


def set_90_sp(sps=295):
    global SP_FOR_90_DEG_TURN
    SP_FOR_90_DEG_TURN = sps


def main():
    print(
        " wheel circumference {}\n".format(WHEEL_CIRCUMFERENCE),
        "wheel rotations/cm {}\n".format(ROTATIONS_PER_CM),
        "wheel rotations/deg {}\n".format(ROTATIONS_PER_DEGREE),
    )

if __name__ == "__main__":
    main()
