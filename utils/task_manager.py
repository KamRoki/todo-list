import json
import os

# path to tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    '''
    Load tasks from the JSON file.
    '''
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    '''
    Save a single task to the JSON file.
    '''
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent = 2)