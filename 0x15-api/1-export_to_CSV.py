#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""

import requests
import csv
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    input_variable = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            my_writer.writerow([int(userId), user.get('username'),
                                task.get('completed'),
                                task.get('title')])
