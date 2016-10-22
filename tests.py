import requests
from time import sleep

HOST = 'http://localhost:8080'

print('List all user ids GET -----------------------')
r = requests.get(HOST + '/api/user')
print r.json()

print('List all line entry ids GET -----------------------')
r = requests.get(HOST + '/api/lineentry')
print r.json()

print('Make a new user POST -----------------------')
payload = {'first_name': 'Burt', 'last_name': 'Reynolds', 'email': 'd@d.com', 'password': '1', 'user_type': 'user'}
r = requests.post(HOST + '/api/user', params=payload)
print r.json()

student = r.json()['id']
print student

print('Make a new line entry PUT -----------------------')
r = requests.put(HOST + '/api/lineentry/user/' + str(student))
print r.json()

sleep(4)

print('Delete user with DELETE -----------------------')
r = requests.delete(HOST + '/api/user/' + str(student))

print('List all user ids GET -----------------------')
r = requests.get(HOST + '/api/user')
print r.json()

print('List all line entry ids GET -----------------------')
r = requests.get(HOST + '/api/lineentry')
print r.json()
