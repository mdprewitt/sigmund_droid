import requests
import json
import pprint

url = 'http://127.0.0.1:5000/api/person'
headers = {'Content-Type': 'application/json'}

filters = [dict(
    name='sid',
    op='==',
    val='m123456'
)]
params = dict(q=json.dumps(dict(filters=filters, single=True)))

response = requests.get(url, params=params, headers=headers)
assert response.status_code == 200
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(response.json())
