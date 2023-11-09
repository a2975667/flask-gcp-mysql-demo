"""Defines all the functions related to the database"""
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks;")
    todo_list = []
    for result in cursor:
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
    cursor.close()
    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    cursor = db.cursor()
    query = 'UPDATE tasks SET task = "{}" WHERE id = {};'.format(text, task_id)
    cursor.execute(query)
    db.commit()
    cursor.close()


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """

    cursor = db.cursor()
    query = 'UPDATE tasks SET status = "{}" WHERE id = {};'.format(text, task_id)
    cursor.execute(query)
    db.commit()
    cursor.close()


def insert_new_task(text: str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    cursor = db.cursor()
    query = 'INSERT INTO tasks (task, status) VALUES ("{}", "{}");'.format(text, "Todo")
    cursor.execute(query)
    cursor.execute("SELECT LAST_INSERT_ID();")
    query_results = [x for x in cursor]
    task_id = query_results[0][0]
    db.commit()
    cursor.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    cursor = db.cursor()
    query = 'DELETE FROM tasks WHERE id={};'.format(task_id)
    cursor.execute(query)
    db.commit()
    cursor.close()
