from enum import Enum

BASEURL = "https://todo.pixegami.io/"
NOT_FOUND =  404
OK = 200
NUMBER_OF_TASKS = 3

class EndPoints(Enum):
    CREATE_TASK = BASEURL + "create-task"
    GET_TASK = BASEURL + "get-task/"
    LIST_TASKS = BASEURL + "list-tasks/"
    UPDATE_TASK = BASEURL + "update-task"
    DELETE_TASK = BASEURL + "delete-task/"




