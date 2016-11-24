#!/usr/bin/python

import requests
from time import sleep

HOST = 'http://localhost:8080'

# print('Invalid Login POST -----------------------')
# payload = {'email': 'admin@gmail.com', 'password': '1235'}
# r = requests.post(HOST + '/api/login', params=payload)
# print r.json()

print('Valid Login POST -----------------------')
payload = {'email': 'admin@gmail.com', 'password': '1'}
r = requests.post(HOST + '/api/login', params=payload)
# print r.json()
token = r.json()['token']
print token
