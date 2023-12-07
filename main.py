#!/usr/bin/env python3

import json
import os
from pprint import PrettyPrinter
from classes.task import Task

if __name__ == "__main__":
    pp = PrettyPrinter(indent=4)

    print(os.path.dirname(os.path.abspath(__file__)))

    task = Task()

    cwd = os.path.dirname(__file__)
    CREATE_TASKS_FILE = '/data/tasks/create_tasks.json'

    file = open(f'{cwd}{CREATE_TASKS_FILE}',  encoding="UTF-8")
    create_task_data = json.load(file)['tasks']

    UPDATE_TASKS_FILE = '/data/tasks/update_tasks.json'
    file = open(f'{cwd}{UPDATE_TASKS_FILE}',  encoding="UTF-8")
    update_task_data = json.load(file)['updated_tasks_bodies']

    message = get_message()
    print('API STATE')
    print(message, end='\n\n')

    tasks_iterator = iter(create_task_data)

    task_info = next(tasks_iterator)
    create_task_response = task.create(task_info)

    print('CREATE TASK')
    print(create_task_response.json(), end='\n\n')

    just_created_task = create_task_response.json()['task']
    just_created_task_id = just_created_task['task_id']
    user_id = just_created_task['user_id']

    just_created_task = get_task_by_id(just_created_task_id)

    print('GET TASK BY ID')
    print(just_created_task.json(), end='\n\n')

    listed_tasks = get_tasks_list(user_id)
    tasks = listed_tasks.json()['tasks']

    print('GET TASKS LIST')
    for task_info in tasks:
        print(task_info, end='\n\n')

    updated_task = task.update(just_created_task_id, update_task_data[0])

    print('UPDATE TASK')
    print(updated_task.json(), end='\n\n')

    just_updated_task = updated_task.json()['task']
    just_updated_task_id = just_updated_task['task_id']

    just_updated_task = get_task_by_id(just_created_task_id)

    print('GETTING JUST UPDATED TASK')
    print(just_updated_task.json(), end='\n\n')

    deleted_task = task.delete(just_created_task_id)

    print('DELETE TASK')
    print(deleted_task.json(), end='\n\n')


    cwd = os.path.dirname(__file__)
    CREATE_TASKS_FILE = '/data/tasks/create_tasks.json'

    file = open(f'{cwd}{CREATE_TASKS_FILE}',  encoding="UTF-8")
    create_task_data = json.load(file)['tasks']

    UPDATE_TASKS_FILE = '/data/tasks/update_tasks.json'
    file = open(f'{cwd}{UPDATE_TASKS_FILE}',  encoding="UTF-8")
    update_task_data = json.load(file)['updated_tasks_bodies']

    message = get_message()
    print('API STATE')
    print(message, end='\n\n')

    tasks_iterator = iter(create_task_data)

    task_info = next(tasks_iterator)
    create_task_response = task.create(task_info)

    print('CREATE TASK')
    print(create_task_response.json(), end='\n\n')

    just_created_task = create_task_response.json()['task']
    just_created_task_id = just_created_task['task_id']
    user_id = just_created_task['user_id']

    just_created_task = get_task_by_id(just_created_task_id)

    print('GET TASK BY ID')
    print(just_created_task.json(), end='\n\n')

    listed_tasks = get_tasks_list(user_id)
    tasks = listed_tasks.json()['tasks']

    print('GET TASKS LIST')
    for task_info in tasks:
        print(task_info, end='\n\n')

    updated_task = task.update(just_created_task_id, update_task_data[0])

    print('UPDATE TASK')
    print(updated_task.json(), end='\n\n')

    just_updated_task = updated_task.json()['task']
    just_updated_task_id = just_updated_task['task_id']

    just_updated_task = get_task_by_id(just_created_task_id)

    print('GETTING JUST UPDATED TASK')
    print(just_updated_task.json(), end='\n\n')

    deleted_task = task.delete(just_created_task_id)

    print('DELETE TASK')
    print(deleted_task.json(), end='\n\n')
