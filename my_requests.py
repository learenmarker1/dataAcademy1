import requests
import json

if __name__ == '__main__':
    r = requests.get("http://127.0.0.1:5000/user")
    dict = r.json()
    for user in dict['users']:
        print(user['name'])



