#!/usr/bin/env python3

from ev3dev.ev3 import *
from navigation import speak, abort_on_button, sleep
from setup_sample_data import people
import ev3dev.ev3 as ev3
from PIL import Image
import logging

import requests
import json


LOGGER = logging.getLogger(__name__)

def setup_color_sensor(mode='COL-REFLECT'):

    #connect color sensor and check it's connected.
    cl = ColorSensor()
    assert cl.connected

    cl.mode = mode

    return cl


@abort_on_button
def get_color(url="http://127.0.0.1:5000", fake_data=False):
    """
    gets numerical color value from color sensor
    sends value to directory api to retrieve person details
    :param url: host:port url of api server
    :return: set of coordinates for desk
    """

    cl = setup_color_sensor('COL-COLOR')

    color = cl.value()
    while color < 1:
        LOGGER.debug("Waiting to read color")
        color = cl.value()
        sleep(.1)

    # change the sensor mode which makes it emit a red light so we know it's read something
    cl.mode= 'COL-REFLECT'

    LOGGER.debug("looking for person with sid=%d", color)

    if fake_data:
        LOGGER.debug("using mock data")
        person = people[color]
        person_name = '{} {}'.format(person['first'], person['last'])
        coordinates = (person['location_x'], person['location_y'])
    else:
        try:
            filters = [dict(
                name='sid',
                op='==',
                val=str(color),
            )]
            params = dict(q=json.dumps(dict(filters=filters, single=True)))
            headers = {'Content-Type': 'application/json'}

            LOGGER.debug("Making request [%s] params=[%s]", url, params)

            result = requests.get(
                url="{url}/api/person".format(url=url),
                params=params,
                headers=headers,
            )
            if result.status_code == 404:
                LOGGER.error("Person [%s] not found", color)
                raise Exception
            elif result.status_code != 200:
                LOGGER.error("Query error %s - %s", result.status_code, result.reason)
                raise Exception
        except:
            LOGGER.exception("Exception making request")
            raise

        person = json.loads(result.content.decode('utf-8'))
        person_name = '{} {}'.format(person['first'], person['last'])
        coordinates = (person['desk']['location_x'], person['desk']['location_y'])

    LOGGER.debug("Person=%s, x=%s, y=%s", person_name, coordinates[0], coordinates[1])

    message = "Ah Taking you to {}".format(person_name)
    speak(message)

    return coordinates
