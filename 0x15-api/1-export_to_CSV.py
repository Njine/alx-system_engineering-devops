filename = '{}.csv'.format(userid)
with open(filename, mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    employee_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    for task in tasks_json:
        employee_writer.writerow([
            userid,
            username,
            task.get('completed'),
            task.get('title')
        ])
