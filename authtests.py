#!/usr/bin/python

import requests
from time import sleep

HOST = 'http://localhost:8080'

print('Make a new user POST -----------------------')
payload = {'email': 'admin@gmail.com', 'password': '1235'}
r = requests.post(HOST + '/api/login', params=payload)
print r.json()

print('Make a new user POST -----------------------')
payload = {'email': 'admin@gmail.com', 'password': '1'}
r = requests.post(HOST + '/api/login', params=payload)
print r.json()
