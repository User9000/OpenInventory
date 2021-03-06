import requests
ENDPOINT = "http://127.0.0.1:5555/api/status/52/"
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

#POSTING AN IMAGE TO THE REST-API
#do_img(method='post', data={'user': 1, "content": "test"}, is_json=False, img_path=image_path)
#do(data={'id': 13})
#do(method='post', data={'content': "some new cool content", 'user': 1})
#do(method='put', data={'id': 13, "content": "some new cool content", "user": 1})
#get_endpoint = ENDPOINT +  str(16)

post_headers = {
        'Content-Type': 'application/json',
        #'Authorization': "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNSwidXNlcm5hbWUiOiJhZG1pbjE3IiwiZXhwIjoxNjEwMzQzODg2LCJlbWFpbCI6ImFkbWluMTdAaG90bWFpbC5jb20iLCJvcmlnX2lhdCI6MTYxMDM0MzU4Nn0.0B1aje9kKpOhYGe7IafDsm_ekVSDEYXHssyYHj7LeqI',

}

data  = {

    'username' : 'admin14',
    'password': 'localuser1!',
        'password2': 'localuser1!',
        'email': 'admin14@hotmail.com'
}

AUTH_ENDPOINT = 'http://127.0.0.1:5555/api/auth/jwt/'
#AUTH_ENDPOINT = 'http://127.0.0.1:5555/api/auth/register/'


r1 = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=post_headers)

#print(r1.json())
token = r1.json()['token']
headers2 = {
    #"Content-Type": "application/json",
    "Authorization": "JWT "  + token
}
data2 =  { 
    'content' : 'this new content post'
}

with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r2 = requests.get(ENDPOINT, data=data2, headers=headers2)


#r2 = requests.post(ENDPOINT, data=json.dumps(data2), headers=headers2)
            print(r2.text)
# user_from_app = r1.json()['username']
# auth_expiration_data = r1.json()['expiration']
# print(token, user_from_app, auth_expiration_data)
# headers = {
#     #"Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }
#posted_response = requests.post(ENDPOINT,data=post_data, headers=headers )
#r1 = requests .get(get_endpoint)
#print(posted_response.text)
#r2 = requests.put(ENDPOINT, data=post_data, headers=post_headers)

# with open(image_path, 'rb') as image:
#     file_data = {
#                 'image': image
#             }

#     data ={
#         "content": "random data"
#         }
#     r = requests.post(ENDPOINT, data=data, headers=headers, files=file_data)
#     print(r.text)





# with open(image_path, 'rb') as image:
#     file_data = {
#                 'image': image
#             }

#     data ={
#         "content": "random data"
#         }
#     json_data = json.dumps(data)
#     r = requests.put(ENDPOINT + str(37) + "/", data=data, headers=headers, files=file_data)
#     print(r.text)