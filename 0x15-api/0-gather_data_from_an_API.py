#!/usr/bin/python3

'''Retrieves employee data from API using employee ID.'''

import requests
import sys


def fetch_data(employee_id):
    '''Gets employee data: [name, ID, [completed_tasks], [all_tasks]].'''
    data = ['', 0, [], []]
    try:
        user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos').json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
