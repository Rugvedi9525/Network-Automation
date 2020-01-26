import requests
import json

list_todos = []
todos = requests.get('https://jsonplaceholder.typicode.com/todos')
list_todos = todos.json()


for todo in list_todos:
    if todo['completed'] == True:
        print (todo)
