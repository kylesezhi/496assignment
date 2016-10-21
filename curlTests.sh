echo 'List all users -----------------------'
curl http://localhost:8080/api/user
echo

# echo 'Make new user -----------------------'
# curl --data-urlencode "first_name=Burt" --data-urlencode "last_name=Reynolds" --data-urlencode "email=d@d.com" --data-urlencode "password=123" http://localhost:8080/api/user
# echo

echo 'List all line entries -----------------------'
curl http://localhost:8080/api/lineentry
echo

echo 'Make new line entry'
curl --data-urlencode "user=4572868859920384" http://localhost:8080/api/lineentry
echo
