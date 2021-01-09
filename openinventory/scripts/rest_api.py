import requests
ENDPOINT = "http://127.0.0.1:5555/api/status/"

import os

import json

image_path = os.path.join(os.getcwd(), "prius.PNG")

os.environ['NO_PROXY'] = '127.0.0.1'


def do(method='get', data={}, is_json=True):
    headers = {}

    if is_json:
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data)
    print(r.text)
    return r


def do_img(method='get', data={}, is_json=True, img_path=None):
    
    if is_json:
        
        data = json.dumps(data)

    if img_path is not None:
        with open(img_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data)
    else:
         r = requests.request(method, ENDPOINT, data=data)

        

    
    print(r.text)
    print(r.status_code)
    return r


do_img(method='post', data={'user': 1, "content": "test"}, is_json=False, img_path=image_path)

#do(data={'id': 13})
#do(method='post', data={'content': "some new cool content", 'user': 1})
#do(method='put', data={'id': 13, "content": "some new cool content", "user": 1})



