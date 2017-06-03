from math import pi
from ev3dev.ev3 import (
    LargeMotor,
    OUTPUT_C,
    OUTPUT_B,
    OUTPUT_A,
    MediumMotor,
)


X_POSITION = 0
Y_POSITION = 0

RED_DESK = tuple([30, 20])
BLUE_DESK = tuple([30, -20])

WHEEL_DIAMETER = 5.6  # centimeters
WHEEL_CIRCUMFERENCE = pi * WHEEL_DIAMETER
ROTATIONS_PER_CM = 1 / WHEEL_CIRCUMFERENCE
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

def main ():
    print(
        " wheel circumference {}\n".format(WHEEL_CIRCUMFERENCE),
        "wheel rotations/cm {}\n".format(ROTATIONS_PER_CM),
        "wheel rotations/deg {}\n".format(ROTATIONS_PER_DEGREE),
    )

if __name__ == "__main__":
    main()