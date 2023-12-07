import json
from config import PROJECT_ROOT_DIR


def load_fixtures(filename):
    file_path = f'{PROJECT_ROOT_DIR}/data/tasks/{filename}'
    file = open(f'{file_path}', encoding='UTF-8')
    data = json.load(file)
    return data
