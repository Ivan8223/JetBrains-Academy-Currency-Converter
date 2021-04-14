# write your code here
with open('users.json', 'r') as users_json_file:
    print(len(json.load(users_json_file)['users']))
