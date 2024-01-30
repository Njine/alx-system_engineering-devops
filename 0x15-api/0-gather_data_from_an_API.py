#!/usr/bin/python3
'''Fetches employee data from API using employee ID.'''
import requests
import sys

def fetch_data(employee_id):
    '''Fetches employee data using ID in the format: [name, ID, [completed_tasks], [all_tasks]].'''
    data = ['', 0, [], []]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    data[0] = user.get('name')
    data[1] = user.get('id')
    for todo in todos:
        if todo.get('userId') == user.get('id'):
            data[3].append(todo)
            if todo.get('completed'):
                data[2].append(todo)
    return data

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    data = fetch_data(employee_id)
    print(f'Employee {data[0]} is done with tasks({len(data[2])}/{len(data[3])}):')
    for todo in data[2]:
        print(f'\t{todo.get("title")}')


if __name__ == '__main__':
    main()
