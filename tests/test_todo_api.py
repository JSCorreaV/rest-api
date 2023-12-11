import tests.api.Callers as Callers
import tests.fixtures.Payload as payload
import tests.utils.Constants as const

def test_can_call_endpoint():
    response = Callers.health_check()
    assert response.status_code == const.OK
    
def test_can_create_task():
    task_payload = payload.new_task_payload()
    create_task_response = Callers.create_task(task_payload)
    assert create_task_response.status_code == const.OK
    create_task_data = create_task_response.json()

    task_id = create_task_data["task"]["task_id"]
    get_task_response = Callers.get_task(task_id)
    assert get_task_response.status_code == const.OK
    get_task_data = get_task_response.json()

    assert get_task_data["content"] == task_payload["content"]
    assert get_task_data["user_id"] == task_payload["user_id"]

def test_can_update_task():
    task_payload = payload.new_task_payload()
    create_task_response = Callers.create_task(task_payload)
    task_id = create_task_response.json()["task"]["task_id"]

    new_payload = task_payload
    new_payload["task_id"] = task_id
    new_payload["content"] = "updated test_content"
    new_payload["is_done"] = True

    update_task_response = Callers.update_task(new_payload)
    assert update_task_response.status_code == const.OK
    
    get_task_response = Callers.get_task(task_id)
    assert get_task_response.status_code == const.OK
    get_task_data = get_task_response.json()
    
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]
    
def test_can_list_tasks():
    number_of_tasks = 3
    payload = payload.new_task_payload()
    for _ in range(number_of_tasks):
        create_task_response = Callers.create_task(payload)
        assert create_task_response.status_code == const.OK
    
    list_tasks_response = Callers.list_tasks(payload["user_id"])
    assert list_tasks_response.status_code == const.OK
    list_tasks_data = list_tasks_response.json()
    assert len(list_tasks_data["tasks"]) == number_of_tasks

def test_can_delete_task():
    task_payload = payload.new_task_payload()
    create_task_response = Callers.create_task(task_payload)
    assert create_task_response.status_code == const.OK
    
    task_id = create_task_response.json()["task"]["task_id"]
    delete_task_response = Callers.delete_task(task_id)
    assert delete_task_response.status_code == const.OK

    get_task_response = Callers.get_task(task_id)
    assert get_task_response.status_code == const.NOT_FOUND
    

    