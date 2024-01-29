#!/usr/bin/python3
"""
Retrieves employee information using JSONPlaceholder API and writes to CSV
"""

import csv
import requests
import sys


def main():
    """Main function to retrieve and save employee information to CSV"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user_endpoint = '{}users/{}'.format(url, userid)
    response = requests.get(user_endpoint)

    if response.status_code != 200:
        print("Error: Unable to retrieve user data")
        sys.exit(1)

    user_data = response.json()
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

    filename = '{}.csv'.format(userid)
    with open(filename, mode='w', newline='') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        employee_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks_json:
            employee_writer.writerow([userid, username, task.get('completed'), task.get('title')])


if __name__ == "__main__":
    main()
