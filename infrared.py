#!/usr/bin/env python3
#If you use the infrared sensor in place of the ultrasound sensor then you must modify the code since these sensors use different commands to obtain the sensor reading and since the infrared sensor returns a value that is neither in cm nor in mm. To convert an IR value into a very approximate distance in cm, multiply the IR value by 0.7. For example, if the IR value is 100 then the distance is roughly 70 cm. That means 11 cm corresponds to 16 'IR units' and 5 cm corresponds to 7 'IR units'. Here is the same program, modified for the IR sensor. Changed lines are highlighted.
from ev3dev.ev3 import *
from time import sleep

# Connect infrared sensor to any sensor port
# and check it is connected.
ir = InfraredSensor() 
assert ir.connected, "Connect an IR sensor to any sensor port"

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

# Record the initial separation of the sensor and the object
startdistance = ir.value()

# Advance at 50% speed (speed_sp=450)
mB.run_forever(speed_sp=-450)
mC.run_forever(speed_sp=-450)

# Wait until robot has moved (at least) 11 cm closer
# to the reflecting object in front of it
while ir.value() > startdistance-16:  # 16 IR units = 11cm approx
    sleep(0.01)
    
# Turn off the motors and apply the brake
mB.stop(stop_action="brake")
mC.stop(stop_action="brake")

sleep(1)

# Reverse at 50% speed
mB.run_forever(speed_sp=450)
mC.run_forever(speed_sp=450)

# Wait until robot is less than 5 cm from its starting position
while ir.value() < startdistance-7:  # 7 IR units = 5cm approx
    sleep(0.01)
    
mB.stop()
mC.stop()
