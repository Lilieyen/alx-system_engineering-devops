#!/usr/bin/python3
"""
export to json
"""

import requests
import json
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.json".format(userId), "w") as json_file:
        json.dump({userId: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")} for task in todo]}, json_file)
