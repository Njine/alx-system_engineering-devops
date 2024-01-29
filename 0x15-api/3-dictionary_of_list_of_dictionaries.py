#!/usr/bin/python3
"""
Retrieve employee information using JSONPlaceholder API and save to JSON
"""

import json
import requests
import sys


def main():
    """Main function to retrieve and save employee information"""
    url = 'https://jsonplaceholder.typicode.com/'
    users_endpoint = '{}users'.format(url)
    response = requests.get(users_endpoint)
    users_data = response.json()
    tasks_dict = {}

    for user_data in users_data:
        name = user_data.get('username')
        userid = user_data.get('id')
        todos_endpoint = '{}todos?userId={}'.format(url, userid)
        tasks_response = requests.get(todos_endpoint)
        tasks_data = tasks_response.json()
        user_tasks = []

        for task_data in tasks_data:
            task_dict = {"username": name,
                         "task": task_data.get('title'),
                         "completed": task_data.get('completed')}
            user_tasks.append(task_dict)

        tasks_dict[str(userid)] = user_tasks

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file:
        json.dump(tasks_dict, file)


if __name__ == "__main__":
    main()
