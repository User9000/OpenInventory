import requests
ENDPOINT = "http://127.0.0.1:5555/api/status/"

import os

import json

os.environ['NO_PROXY'] = '127.0.0.1'


def do(method='get', data={}, is_json=True):

    if is_json:
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data)
    print(r.text)
    return r


do(data={'id': 1})
