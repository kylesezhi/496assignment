# echo 'List all users GET -----------------------'
# curl http://localhost:8080/api/user
# echo

# echo 'Make new user -----------------------'
# curl --data-urlencode "first_name=Burt" --data-urlencode "last_name=Reynolds" --data-urlencode "email=d@d.com" --data-urlencode "password=123" http://localhost:8080/api/user
# echo

# echo 'List all line entries GET -----------------------'
# curl http://localhost:8080/api/lineentry
# echo

# echo 'Make new line entry POST -----------------------'
# curl --data-urlencode "user=4572868859920384" http://localhost:8080/api/lineentry
# echo

# echo 'Make new line entry with PUT -----------------------'
# curl -X PUT http://localhost:8080/api/lineentry/user/4572868859920384
# echo

echo 'Delete user with DELETE -----------------------'
curl -X DELETE http://localhost:8080/api/user/5663034638860288
echo
