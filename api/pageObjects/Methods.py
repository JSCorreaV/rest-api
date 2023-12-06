import requests
import json

jsonFile = open('api/fixtures/CommonData.json')
data = json.load(jsonFile)
applicationJsonHeader = 'application/json'
baseUrl = data["baseUrl"]
succesfulMessage = data["succesfulMessage"]
nonSuccesfulMessage = data["nonSuccesfulMessage"]

def testConection():
    return requests.get(baseUrl)

def createTask(creationBodyData):
    content = creationBodyData["content"]
    userId = creationBodyData["user_id"]
    isDone = creationBodyData["is_done"]
    url = baseUrl + 'create-task'
    task = json.dumps({
        "content": content,
        'user_id': userId,
        'is_done': isDone
        })
    headers = {
        'accept': applicationJsonHeader,
        'Content-Type': applicationJsonHeader
        }

    response = requests.put(url, headers = headers, data = task)
    return response
    
def getTaskById(taskId):
    url = baseUrl + 'get-task/' + taskId
    headers = {
        'accept': applicationJsonHeader
        }

    response = requests.get(url, headers = headers)
    return response

def getTasksByUserId(userId):
    url = baseUrl + 'list-tasks/' + userId
    headers = {
        'accept': applicationJsonHeader
        }
    response = requests.get(url, headers = headers)
    return response

###########

def deleteTaskById(taskId):
    url = baseUrl + 'delete-task/' + taskId
    headers = {
        'accept': applicationJsonHeader
        }
    response = requests.delete(url, headers = headers)
    if response.status_code == 200:
        print(succesfulMessage)
        print('Task ' + taskId + ' deleted')
    else:
        print('Error ' + str(response.status_code))

def updateTask(creationBodyData):
    taskId = creationBodyData["task_id"]

    taskResponse = getTaskById(taskId)

    if creationBodyData["content"] != '':
        content = creationBodyData["content"]
    else:
        content = taskResponse["content"]
        
    if creationBodyData["user_id"] != '':
        userId = creationBodyData["user_id"]
    else:
        content = taskResponse["content"]

    if creationBodyData["is_done"] != '':
        isDone = creationBodyData["is_done"]
    else:
        content = taskResponse["content"]
    
    url = baseUrl + 'update-task'
    task = json.dumps({
        "content": content,
        'user_id': userId,
        "task_id": taskId,
        'is_done': isDone
        })
    headers = {
        'accept': applicationJsonHeader,
        'Content-Type': applicationJsonHeader
        }

    response = requests.put(url, headers = headers, data = task)
    if response.status_code == 200:
        task_id = response.json()['task']['task_id']
        print(succesfulMessage)
        print('Task ' + task_id + ' updated')
        return response
    else:
        print('Conection Failed')