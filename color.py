#!/usr/bin/env python3

from ev3dev.ev3 import *
from navigation import speak, abort_on_button
import ev3dev.ev3 as ev3
from time import sleep
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

    ready = True

    while ready:

        dest = cl.value()
        while dest < 1:
            dest = cl.value()
            sleep(.1)

        LOGGER.debug("looking for person with sid=%d", dest)

        try:
            filters = [dict(
                name='sid',
                op='==',
                val=str(dest),
            )]
            params = dict(q=json.dumps(dict(filters=filters, single=True)))
            headers = {'Content-Type': 'application/json'}

            LOGGER.debug("Making request [%s] params=[%s]", url, params)

            result = requests.get(
                url="{url}/api/person".format(url=url, dest=str(dest)),
                params=params,
                header=headers,
            )
            ready = False
        except:
            raise Exception("User does not exist")

    person = json.loads(result.content.decode('utf-8'))
    coordinates = (person['desk']['location_x'], person['desk']['location_y'])

    message = ("Taking you to {} {}".format(person['first'], person['last']))
    speak(message)

    return coordinates