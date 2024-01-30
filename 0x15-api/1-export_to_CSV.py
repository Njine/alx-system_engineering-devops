#!/usr/bin/python3
""" Retrieves employee information using JSONPlaceholder API and writes to CSV """

import csv
import requests
import sys


if __name__ == "__main__":
    # API base URL
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Retrieve user ID from command line argument
    user_id = sys.argv[1]

    # Retrieve user data
    user_endpoint = '{}users/{}'.format(base_url, user_id)
    response_user = requests.get(user_endpoint)
    user_data = response_user.json()

    # Extract username from user data
    username = user_data.get('username')

    # Retrieve tasks for the user
    todos_endpoint = '{}todos?userId={}'.format(base_url, user_id)
    response_tasks = requests.get(todos_endpoint)
    tasks_data = response_tasks.json()

    # Prepare data for CSV
    csv_data = []
    for task in tasks_data:
        csv_data.append([
            user_id,
            username,
            task.get('completed'),
            task.get('title')
        ])

    # Write data to CSV file
    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task_row in csv_data:
            csv_writer.writerow(task_row)
