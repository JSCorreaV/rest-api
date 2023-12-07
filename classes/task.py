from config import API_URL
from requests import get, put, delete
from constants.constants import timeouts, endpoints


class Task:
    def __init__(self, body):
        self.body = body
        self.response = self.create().json()['task']

    @staticmethod
    def get_message():
        get_request = get(API_URL, timeout=timeouts["LONG_TIMEOUT"])
        return get_request

    @staticmethod
    def create_task(body):
        create_task_request = put(endpoints['CREATE_TASK'],
                                  json=body,
                                  timeout=timeouts["LONG_TIMEOUT"])
        return create_task_request

    @staticmethod
    def get_task_by_id(task_id):
        get_task_by_id_request = get(f'{endpoints["GET_TASK"]}{task_id}',
                                     timeout=timeouts["LONG_TIMEOUT"])
        return get_task_by_id_request

    @staticmethod
    def get_tasks_list(user_id):
        get_tasks_list_request = get(f'{endpoints["LIST_TASKS"]}{user_id}',
                                     timeout=timeouts["LONG_TIMEOUT"])
        return get_tasks_list_request

    @staticmethod
    def update_specific_task(task_id, updated_body):
        updated_body.update({task_id: task_id})
        update_task_request = put(f'{endpoints["CREATE_TASK"]}',
                                  json=updated_body,
                                  timeout=timeouts["LONG_TIMEOUT"])
        return update_task_request

    @staticmethod
    def delete_specific_task(task_id):
        delete_task_request = delete(f'{endpoints["DELETE_TASK"]}{task_id}',
                                     timeout=timeouts["LONG_TIMEOUT"])
        return delete_task_request

    def get(self):
        print(self.body)
        print(self.response)
        get_task_request = get(f'{endpoints["GET_TASK"]}{self.response["task_id"]}').json()
        print(get_task_request)
        return get_task_request

    def create(self):
        create_task_request = put(endpoints['CREATE_TASK'],
                                  json=self.body,
                                  timeout=timeouts["LONG_TIMEOUT"])
        return create_task_request

    def update(self):
        update_task_request = put(endpoints['UPDATE_TASK'],
                                  json=self.body,
                                  timeout=timeouts["LONG_TIMEOUT"])
        return update_task_request

    def delete(self):
        delete_task_request = delete(f'{endpoints["DELETE_TASK"]}{self.response["task_id"]}',
                                     timeout=timeouts["LONG_TIMEOUT"])
        return delete_task_request
