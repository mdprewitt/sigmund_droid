#!/usr/bin/env python3

from ev3dev.ev3 import *
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


def get_color():
    """
    gets numerical color value from color sensor
    sends value to directory api to retrieve person details
    :return: set of coordinates for desk
    """

    cl = setup_color_sensor()

    ready = True

    while ready:

        dest = cl.value()
        print("looking for desk #%d", dest)

        url = "http://127.0.0.1:5000/api/person/" + str(dest) # TODO read from config

        try:
            result = requests.get(url=url)
            ready = False
        except:
            Exception("User does not exist")

    person = json.loads(result.content.decode('utf-8'))
    coordinates = (person['desk']['location_x'], person['desk']['location_y'])

    message = ("Taking you to %s %s", person['first'], person['last'])
    speak(message)

    return coordinates