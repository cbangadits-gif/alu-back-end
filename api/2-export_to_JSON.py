#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": user_id}
    ).json()

    username = user.get("username")
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
