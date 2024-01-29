#!/usr/bin/python3
"""Retrieves employee information using JSONPlaceholder API and writes to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user_endpoint = '{}users/{}'.format(url, userid)
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    username = user_data.get('username')

    todos_endpoint = '{}todos?userId={}'.format(url, userid)
    tasks_response = requests.get(todos_endpoint)
    tasks_json = tasks_response.json()
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
