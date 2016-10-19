echo 'Test list all users -----------------------'
curl http://localhost:8080/api/user
echo

# echo 'Test make new user -----------------------'
# curl --data-urlencode "first_name=Burt" --data-urlencode "last_name=Reynolds" --data-urlencode "email=d@d.com" --data-urlencode "password=123" http://localhost:8080/api/user
# echo
