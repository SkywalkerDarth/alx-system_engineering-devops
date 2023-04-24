#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python script that, using a REST API exports JSON
"""
from requests import get
from json import dump

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    dic = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        dic[user_id] = []
        for task in tasks:
            dic[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username})

    with open('todo_all_employees.json', 'w') as file:
        dump(dic, file)
