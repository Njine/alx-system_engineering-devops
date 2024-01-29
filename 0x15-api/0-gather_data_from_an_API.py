#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_response.json()

    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    employee_name = None
    completed_tasks = 0
    total_tasks = 0
    task_titles = []

    for user in users_data:
        if user.get('id') == employee_id:
            employee_name = user.get('name')
            break

    if employee_name is None:
        print("Error: Employee ID not found")
        sys.exit(1)

    for todo in todos_data:
        if todo.get('userId') == employee_id:
            total_tasks += 1
            if todo.get('completed'):
                completed_tasks += 1
                task_titles.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for title in task_titles:
        print("\t{}".format(title))
