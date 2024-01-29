#!/usr/bin/python3
"""Retrieves employee information using JSONPlaceholder API and writes to CSV"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user_endpoint = '{}users/{}'.format(url, userid)
    response = requests.get(user_endpoint)
    user_data = response.json()
    username = user_data.get('username')

    todos_endpoint = '{}todos?userId={}'.format(url, userid)
    tasks_response = requests.get(todos_endpoint)
    tasks_json = tasks_response.json()
    tasks_list = []

    for task in tasks_json:
        tasks_list.append([userid,
                           username,
                           task.get('completed'),
                           task.get('title')])

    filename = '{}.csv'.format(userid)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in tasks_list:
            employee_writer.writerow(task)
