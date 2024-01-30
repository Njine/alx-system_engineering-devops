#!/usr/bin/python3
'''Fetches employee data from API using employee ID.'''
import requests
from sys import argv


def fetch_data(employee_id):
    '''Fetches employee data using ID in the format: [name, ID, [completed_tasks], [all_tasks]].'''
    data = ['', 0, [], []]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id
        )).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    data[0] = user.get('name')
    data[1] = user.get('userId')
    for todo in todos:
        if todo.get('userId') == user.get('id'):
            data[3].append(todo)
            if todo.get('completed'):
                data[2].append(todo)
    return data


if __name__ == '__main__':
    employee_id = argv[1]
    data = fetch_data(employee_id)
    print('Employee {} is done with tasks({}/{}):'.format(
        data[0], len(data[2]), len(data[3])))
    for todo in data[2]:
        print('\t{}'.format(todo.get('title')))
