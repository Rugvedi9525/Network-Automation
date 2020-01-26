import requests
import csv

user_list = (requests.get('https://jsonplaceholder.typicode.com/users')).json()
custom_userlist = []
for user in user_list:
    custom_userlist.append((user['name'], user['address']['city'], (user['address']['geo']['lat'],user['address']['geo']['lng']), user['company']['name']))
print (custom_userlist)

with open('user.csv', 'w') as file:

    writer = csv.writer(file)
    writer.writerow(['name', 'city' ,'GPS coordinates','company name'])
    for user in custom_userlist:
        writer.writerow(user)



