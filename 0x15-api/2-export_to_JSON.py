#!/usr/bin/python3
"""
Retrieves employee information using JSONPlaceholder API and writes to JSON
"""

import json
import requests
import sys


def main():
    """Main function to retrieve and save employee information"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    userid = sys.argv[1]

    try:
        int(userid)
    except ValueError:
        print("User ID must be an integer")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/'

    user_endpoint = '{}users/{}'.format(url, userid)
    user_response = requests.get(user_endpoint)

    if user_response.status_code != 200:
        print("Error: Unable to retrieve user data")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get('username')

    todos_endpoint = '{}todos?userId={}'.format(url, userid)
    tasks_response = requests.get(todos_endpoint)

    if tasks_response.status_code != 200:
        print("Error: Unable to retrieve tasks data")
        sys.exit(1)

    tasks_json = tasks_response.json()

    if not isinstance(tasks_json, list) or not tasks_json:
        print("No tasks found for the given user ID")
        sys.exit(1)

    tasks_list = []

    for task in tasks_json:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        tasks_list.append(task_dict)

    tasks_dict = {str(userid): tasks_list}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as file:
        json.dump(tasks_dict, file)


if __name__ == "__main__":
    main()
