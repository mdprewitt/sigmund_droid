#!/usr/bin/env python3

from ev3dev.ev3 import *
from navigation import speak, abort_on_button, sleep
import ev3dev.ev3 as ev3
from PIL import Image
import logging

import requests
import json


LOGGER = logging.getLogger(__name__)

def setup_color_sensor():

    #connect color sensor and check it's connected.
    cl = ColorSensor()
    assert cl.connected

    #put the color sensor into color mode
    cl.mode= 'COL-COLOR'

    return cl


@abort_on_button
def get_color(url="http://127.0.0.1:5000"):
    """
    gets numerical color value from color sensor
    sends value to directory api to retrieve person details
    :param url: host:port url of api server
    :return: set of coordinates for desk
    """

    cl = setup_color_sensor()

    color = cl.value()
    while color < 1:
        LOGGER.debug("Waiting to read color")
        color = cl.value()
        sleep(.1)

    # change the sensor mode which makes it emit a red light so we know it's read something
    cl.mode= 'COL-REFLECT'

    LOGGER.debug("looking for person with sid=%d", color)

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
    coordinates = (person['desk']['location_x'], person['desk']['location_y'])
    LOGGER.debug("Person=%s, x=%s, y=%s", person['first'], coordinates[0], coordinates[1])

    message = ("Taking you to {} {}".format(person['first'], person['last']))
    speak(message)

    return coordinates
