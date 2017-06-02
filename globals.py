X_POSITION = 0
Y_POSITION = 0

RED_DESK = tuple(30, 20)
BLUE_DESK = tuple(30, -20)

ROTATIONS_PER_CM = .7
ROTATIONS_PER_DEGREE = .5  # how many rotations to turn specified degrees
"""
           0
           |
-90/270 ---|--- 90/-270
           |
       180/-180
"""
DIRECTION = 0 

LEFT_MOTOR = LargeMotor(OUTPUT_A)
RIGHT_MOTOR = LargeMotor(OUTPUT_B)
