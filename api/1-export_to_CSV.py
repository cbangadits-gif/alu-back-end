#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file."""
import csv
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
    filename = "{}.csv".format(user_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
