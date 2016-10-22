import requests

HOST = 'http://localhost'

print('List all user ids GET -----------------------')
r = requests.get(HOST + ':8080/api/user')
print r.json()

print('List all line entry ids GET -----------------------')
r = requests.get(HOST + ':8080/api/lineentry')
print r.json()



# echo 'Make new line entry POST -----------------------'
# curl --data-urlencode "user=4572868859920384" http://localhost:8080/api/lineentry
# echo
