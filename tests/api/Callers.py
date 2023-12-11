import requests
import tests.utils.Constants as const

def health_check():
    return requests.get(const.BASEURL)

def create_task(payload):
    return requests.put(const.EndPoints.CREATE_TASK.value, json=payload)

def get_task(task_id):
    return requests.get(const.EndPoints.GET_TASK.value + task_id)

def list_tasks(user_id):
    return requests.get(const.EndPoints.LIST_TASKS.value + user_id)
    
def update_task(payload):
    return requests.put(const.EndPoints.UPDATE_TASK.value, json=payload)

def delete_task(task_id):
    return requests.delete(const.EndPoints.DELETE_TASK.value + task_id)
