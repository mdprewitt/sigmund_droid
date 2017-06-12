#!/usr/bin/env python3

import os
import argparse
import logging

import globals
from globals import LEDS
from color import get_color as get_target_xy
from navigation import *

LOGGER = logging.getLogger(__name__)


def main(url):
    while True:
        try:
            stop()
            initialize()

            LEDS.set_color(LEDS.LEFT, LEDS.GREEN)
            speak('Welcome to JP Morgan Chase. Who are you looking for?')
            display_image('chase.png')

            x_target, y_target = get_target_xy(url=url)
            moved_right = smart_move(x_target)
            if y_target > 0:
                turn_right()
            else:
                turn_left()
            smart_move(abs(y_target - moved_right))

            LOGGER.info("Reached destination")
            stop()

        except ButtonAbort:
            LOGGER.info("Abort button activated, returning to start")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sigmund Demo.')
    parser.add_argument('--silent', action='store_true')
    parser.add_argument('--log_level', default='INFO')
    parser.add_argument('--url', default='http://{host_ip}:5000'.format(host_ip=os.environ.get('SSH_IP')))
    args = parser.parse_args()

    globals.SILENT = args.silent

    logging.basicConfig(
        format='%(asctime)-15s %(message)s',
        level=args.log_level,
    )

    main(args.url)
