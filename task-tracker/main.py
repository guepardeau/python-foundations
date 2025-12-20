tasks = {}
task_id = 0
title = None
status = None

def add_task(task_id, title, status, tasks):
    task_id += 1
    title = print(input("Please enter a new task: "))
    status = "In Progress"
    tasks[task_id] = {
        "Title": title,
        "Status": status,
    }
    return title, task_id, status, tasks

tasks = add_task(title, task_id, status, tasks)
print(tasks)
