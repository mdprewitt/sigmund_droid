#!/usr/bin/env python3

import os
import sys
import argparse
import logging

sys.path.insert(0, 'directory_app')
import globals
from globals import LEDS
from color import get_color as get_target_xy, setup_color_sensor
from navigation import *

LOGGER = logging.getLogger(__name__)


def main(url, fake_data):
    try:
        stop()
        initialize()
        speak('Press the red button to start the demo.')
    except:
        pass

    wait_for_touch_sensor()
    sleep(1, check=False)

    while True:
        try:
            setup_color_sensor()
            stop()
            initialize()

            LEDS.set_color(LEDS.LEFT, LEDS.GREEN)
            speak('Welcome to JP Morgan Chase. Who are you looking for?')
            display_image('chase.png')

            x_target = None
            while x_target is None:
                try:
                    x_target, y_target = get_target_xy(url=url, fake_data=fake_data)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except ButtonAbort:
                    raise
                except:
                    pass

            moved_right = smart_move(x_target)
            y_adjust = 0
            if y_target > 0:
                turn_right()
                y_adjust = 1
            else:
                turn_left()
                y_adjust = -1
            smart_move(abs(y_target - moved_right))

            LOGGER.info("Reached destination")
            stop()
            speak('Press the red button to return home.')
            wait_for_touch_sensor()
            turn_around()

            moved_right = smart_move(abs(y_target) - y_adjust * 1)
            if y_target > 0:
                turn_left()
            else:
                turn_right()
            smart_move(abs(x_target + moved_right))
            turn_around()

        except ButtonAbort:
            LOGGER.info("Abort button activated, returning to start")
        except (KeyboardInterrupt, SystemExit):
            LOGGER.exception("exit")
            raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sigmund Demo.')
    parser.add_argument('--silent', action='store_true')
    parser.add_argument('--fake_data', action='store_true')
    parser.add_argument('--log_level', default='INFO')
    parser.add_argument('--url', default='http://{host_ip}:5000'.format(host_ip=os.environ.get('SSH_IP')))
    args = parser.parse_args()

    globals.SILENT = args.silent

    logging.basicConfig(
        format='%(asctime)-15s %(message)s',
        level=args.log_level,
    )

    main(args.url, args.fake_data)
