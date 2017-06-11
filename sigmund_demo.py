#!/usr/bin/env python3

import argparse
from time import sleep
import logging

from PIL import Image
import ev3dev.ev3 as ev3
from globals import *
from navigation import *

LOGGER = logging.getLogger(__name__)

# connect infrared and check it's connected.
ir = ev3.InfraredSensor()
assert ir.connected, "Connect a single infrared sensor to port"

# put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

def main():
    initialize()
    ir_distance = ir.value()

    if ir_distance < 500:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        lcd = ev3.Screen()
        logo = Image.open('chase.png')
        lcd.image.paste(logo, (0, 0))
        lcd.update()

        speak('Welcome to JP Morgan Chase. Who are you looking for?')

    else:
        ev3.Leds.all_off()
        sleep(2)

    moved_right = smart_move(75)
    turn_right()
    smart_move(30 - moved_right)

    LOGGER.info("Reached desitnation")
    stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sigmund Demo.')
    parser.add_argument('--silent', action='store_true' )
    parser.add_argument('--log_level', default='INFO')
    args = parser.parse_args()

    global SILENT
    SILENT = args.silent

    logging.basicConfig(
            format='%(asctime)-15s %(message)s',
            level=args.log_level,
            )

    main()
