#!/usr/bin/python

import requests
from time import sleep

HOST = 'http://localhost:8080'

print('Make a new user POST -----------------------')
payload = {'first_name': 'Burt', 'last_name': 'Reynolds', 'email': 'd@d.com', 'password': '1', 'user_type': 'user'}
r = requests.post(HOST + '/api/user', params=payload)
print r.json()
studentid = r.json()['id']
print studentid
