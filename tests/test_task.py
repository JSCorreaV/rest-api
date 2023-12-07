from classes.task import Task
from support.helper import load_fixtures
import copy


class TestTask:

    def setup_method(self, method):
        print(f"Setting up {method}")

        create_tasks_data = load_fixtures(f'create_tasks.json')['tasks']
        first_task = create_tasks_data[0]

        self.task = Task(first_task)

    def teardown_method(self, method):
        print(f"\nTearing down {method}")
        self.task.delete()
        del self.task

    def test_create_task(self):
        response = self.task.create()
        print(response.status_code)
        assert response.status_code == 200

    def test_create_task_with_empty_content(self):
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update({"content": ""})
        response = task_copy.create()
        content = response.json()['task']['content']
        assert content == ''

    def test_create_task_with_none_content(self):
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update({"content": None})
        response = task_copy.create()
        assert response.status_code == 422

    def test_create_task_with_empty_user_id(self):
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update({"user_id": ""})
        response = task_copy.create()
        assert response.status_code == 500

    def test_create_task_with_empty_task_id(self):
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update({"task_id": ""})
        response = task_copy.create()
        assert response.status_code == 500

    def test_create_task_with_none_task_id(self):
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update({"task_id": None})
        response = task_copy.create()
        assert response.status_code == 422

    def test_create_task_with_is_done_set_to_a_string(self):
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update({"is_done": "Random string"})
        response = task_copy.create()
        assert response.status_code == 422

    def test_create_task_with_is_done_set_to_none(self):
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update({"is_done": None})
        response = task_copy.create()
        assert response.status_code == 422

    def test_get_task_has_unchanged_values(self):
        self.task.create()
        task = self.task.get()
        print(task)
        assert task['content'] == self.task.body['content']
        assert task['user_id'] == self.task.body['user_id']
        assert task['is_done'] == bool(self.task.body['is_done'])

    def test_task_can_not_receive_sql_injections(self):
        body = {
            "content": "Inoffensive string",
            "used_id": "&#x53;ELECT user_id, type FROM users WHERE type = admin",
        }
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update(body)
        response = self.task.create()
        assert response.status_code != 200

    def test_task_can_not_be_updated_with_empty_properties(self):
        body = {
            "content": "",
            "used_id": "",
        }
        task_copy = copy.deepcopy(self.task)
        task_copy.body.update(body)
        response = self.task.update()
        assert response.status_code == 200, response.status_code

    def test_delete_task(self):
        response = self.task.delete()
        assert 0, response.status_code

    def test_delete_non_existent_task(self):
        response = Task.delete_specific_task('88238jfyf111')
        assert 0, response.status_code
