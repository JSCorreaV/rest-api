import sys
import json

sys.path.append('api/pageObjects')
import Methods

jsonFileCommon = open('api/fixtures/CommonData.json')
commonData = json.load(jsonFileCommon)
succesfulMessage = commonData['succesfulMessage']
jsonFileCreation = open('api/fixtures/CreationData.json')
creationData = json.load(jsonFileCreation)
bodyData = creationData['creation']

# verifyConection
print('----------Verifing Conection----------')
try:
    conectionResponse = Methods.testConection()
except:
    print('Connection Failed')
else:
    print(str(conectionResponse.status_code) + '! ' + succesfulMessage)

# verifyTaskCreationAndDeletion
print(creationData["initMessage"])

for body in bodyData:
    try:
        creation = Methods.createTask(body)
        taskId = creation.json()['task']['task_id']
    except:
        print('Was not possible create the task.')
        print('In ' + creation.json()['detail'][0]['loc'][0] + ', ' + creation.json()['detail'][0]['loc'][1] + ' ' + creation.json()['detail'][0]['msg'])
    else:
        print('Succesfull Task ' + taskId + ' Created!')
        Methods.deleteTaskById(taskId)

# verifyExistentTask
body = bodyData[0]
creation = Methods.createTask(body)
tasksIds = [creation.json()['task']['task_id'], creationData['fakeTaskId']]

for id in tasksIds:
    try:
        print('----------Verifing Task ' + id + '----------')
        task = Methods.getTaskById(id)
    except:
        #404
        #Undocumented
        #Error: response status is 404
        print(task.json()['detail'])
    else:
        if task.status_code == 200:
            print('Task founded!')
            print(task.json())
        else:
            print(task.json()['detail'])

# verifyExistentTaskByUserId
body = bodyData[0]
creation = Methods.createTask(body)
UsersIds = [creation.json()['task']['user_id'], creationData['fakeUserId']]

for id in UsersIds:
    try:
        print('----------Verifing Task ' + id + '----------')
        task = Methods.getTasksByUserId(id)
    except:
        #Always is 200 even when no data exists
        print(task.json()['detail'])
    else:
        if task.json()['tasks'] != []:
            print('Task founded!')
            print(task.json()['tasks'])
        else:
            print('Tasks with user_id ' + id + ' not founded.')