#!/usr/bin/python3
"""
Retrieves employee TODO list progress using JSONPlaceholder API
"""

import requests
import sys


def gather_todo_list_progress(employee_id):
    """Retrieve and display employee TODO list progress"""
    url = 'https://jsonplaceholder.typicode.com/'

    # Retrieve user data
    user_endpoint = '{}users/{}'.format(url, employee_id)
    response = requests.get(user_endpoint)

    if response.status_code != 200:
        print("Error: Unable to retrieve user data")
        sys.exit(1)

    user_data = response.json()
    username = user_data.get('username')

    # Retrieve tasks data
    todos_endpoint = '{}todos?userId={}'.format(url, employee_id)
    tasks_response = requests.get(todos_endpoint)

    if tasks_response.status_code != 200:
        print("Error: Unable to retrieve tasks data")
        sys.exit(1)

    tasks_json = tasks_response.json()
    total_tasks = len(tasks_json)
    completed_tasks = sum(task.get('completed') for task in tasks_json)

    # Display TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(username, completed_tasks, total_tasks))
    for task in tasks_json:
        if task.get('completed'):
            print("\t{}".format(task.get('title')))


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

    gather_todo_list_progress(employee_id)
