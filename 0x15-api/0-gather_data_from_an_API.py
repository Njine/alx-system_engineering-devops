#!/usr/bin/python3
""" Retrieves employee information using JSONPlaceholder API """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_endpoint = '{}users'.format(url)
    response = requests.get(user_endpoint)
    users_json = response.json()
    tasks_dict = {}

    for user_data in users_json:
        username = user_data.get('username')
        userid = user_data.get('id')
        todos_endpoint = '{}todos?userId={}'.format(url, userid)
        tasks_response = requests.get(todos_endpoint)
        tasks_json = tasks_response.json()
        user_tasks = []

        for task in tasks_json:
            task_dict = {"username": username,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            user_tasks.append(task_dict)

        tasks_dict[str(userid)] = user_tasks

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file:
        json.dump(tasks_dict, file)
