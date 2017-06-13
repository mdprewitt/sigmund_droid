#!/usr/bin/env python3
import requests
import json
import pprint
import argparse
import sys
import color as color


# add arguments to request
parser = argparse.ArgumentParser(description='Get a person from the directory.')
parser.add_argument('--url', default='http://127.0.0.1:5000')
args = parser.parse_args()

# search a person by SID
filters = [dict(
    name='sid',
    op='==',
    val='b123456'
)]

# endpoint
url = 'http://127.0.0.1:5000/api/person'
headers = {'Content-Type': 'application/json'}

# configuration
filters = filters
params = dict(q=json.dumps(dict(filters=filters)))
pp = pprint.PrettyPrinter(indent=4)

# sample query:
# response = requests.get('http://127.0.0.1:5000/api/person?q={"filters":[{"name":"sid","op":"==","val":"b123456"}]}')


def find_color():
    """
         finds color scanned by ev3
         converts numerical value to then SID
      """
    color.setup_color_sensor()
    sid_color= color.get_basic_color()

    if sid_color == '1':
        sid = 'b123456'
    elif sid_color == '2':
        sid = 'a123456'
    return sid


def get_desk_xy(sid):  # color number 1-7

    """
       passes sid from color value from color sensor
       sends value to person endpoint to retrieve person details
       :return: set of coordinates for desk
    """

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        try:
            print("Making request [{}] params=[{}]".format(url, params))
            resp_obj = response.json()
            object_data = resp_obj['objects'][0]
            desk_data = object_data['desk']
            return desk_data['location_x'], (desk_data['location_y'])
        except Exception as e:
            raise e
    else:
        print('There was an error with your request, please try again')

print("Result is {}".format(get_desk_xy(sid='b123456')))
x, y = get_desk_xy(sid='b12456')


