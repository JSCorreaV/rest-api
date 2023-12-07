#!/usr/bin/env python3

from config import API_URL

endpoints = {
    "CREATE_TASK": 'create-task/',
    "GET_TASK": 'get-task/',
    "LIST_TASKS": 'list-tasks/',
    "UPDATE_TASK": 'update-task/',
    "DELETE_TASK": 'delete-task/'
}

endpoints.update({key: f'{API_URL}{value}' for key, value in endpoints.items()})

timeouts = {
    'EXTRA_LONG_TIMEOUT': 1000,
    'LONG_TIMEOUT': 750,
    'MEDIUM_TIMEOUT': 500,
    'SHORT_TIMEOUT': 250,
}
