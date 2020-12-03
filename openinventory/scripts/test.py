import requests

import json

BASE_URL = 'http://127.0.0.1:5555/api/status/'
ENDPOINT = ""

headers = {'User-Agent': 'Mozilla/5.0'}


def get_list(id='15'):  # --> Lists all this out
    data = json.dumps({"id": id})

    req = requests.get(BASE_URL, headers=headers, data=data)
    print(req.status_code)
    status_code = req.status_code

    if status_code != 200:
        print("probably not good sign?")

    data = req.json()

    # for obj in data:

    #     if obj['id'] == 2:

    #         r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
    #         print(r2.json())

    return data


def create_update():  #  --> creates an object in DJANGO database.
    new_data = {'user': 1, "content": "blank"}
    r = requests.post(BASE_URL, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()

    return r.text


def do_obj_update():  #  --> creates an object in DJANGO database.
    new_data = {"id": 2, "content": "SOME NEW AWESOEM"}
    r = requests.put(BASE_URL, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()

    return r.text


def do_obj_delete():  #  --> creates an object in DJANGO database.
    new_data = {"id": 12}
    r = requests.delete(BASE_URL, data=json.dumps(new_data))
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()

    return r.text


print(get_list())
#print(do_obj_delete())
#print(do_obj_update())
#print(create_update())