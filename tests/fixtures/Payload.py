import uuid

def new_task_payload():
    user_id = f"user_{uuid.uuid4().hex}"
    content = f"content_{uuid.uuid4().hex}"
    #print(f"Creating task for user {user_id} with content {content}")

    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }