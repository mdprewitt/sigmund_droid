#!/usr/bin/env python3

from ev3dev.ev3 import *
from navigation import speak, abort_on_button
import ev3dev.ev3 as ev3
from time import sleep
from PIL import Image

import requests
import json


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

        print("looking for desk #%d", dest)

        try:
            result = requests.get(url="{url}/api/person/{dest}".format(url=url, dest=str(dest)))
            ready = False
        except:
            Exception("User does not exist")

    person = json.loads(result.content.decode('utf-8'))
    coordinates = (person['desk']['location_x'], person['desk']['location_y'])

    message = ("Taking you to %s %s", person['first'], person['last'])
    speak(message)

    return coordinates