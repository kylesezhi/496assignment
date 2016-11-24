#!/usr/bin/python

import requests
from time import sleep

HOST = 'http://localhost:8080'

print('Invalid Login POST -----------------------')
payload = {'email': 'admin@gmail.com', 'password': '1235'}
r = requests.post(HOST + '/api/login', params=payload)
print r.json()

print('Valid Login POST -----------------------')
payload = {'email': 'admin@gmail.com', 'password': '1'}
r = requests.post(HOST + '/api/login', params=payload)
token = r.json()['token']
print token

print('Make a new user POST -----------------------')
payload = {'first_name': 'Burt', 'last_name': 'Reynolds', 'email': 'd@d.com', 'password': '1', 'user_type': 'user'}
r = requests.post(HOST + '/api/user', params=payload)
print r.json()
studentid = r.json()['id']
print studentid

print('Make a new line entry POST -----------------------')
payload = {'user': str(studentid), 'token': token }
r = requests.post(HOST + '/api/lineentry', params=payload)
print r.json()

print('Invalid new line entry POST -----------------------')
payload = {'user': str(studentid), 'token': "token" } # wrong token
r = requests.post(HOST + '/api/lineentry', params=payload)
print r

print('Delete user with DELETE -----------------------')
r = requests.delete(HOST + '/api/user/' + str(studentid))
