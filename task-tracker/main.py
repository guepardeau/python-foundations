tasks = {}
task_id = 0
title = None
status = None
prompt_resume = None
resume = None

def add_task(title, status):
    title = input("Please enter a new task: ")
    status = "IN PROGRESS"
    return title, status

def start_stop(prompt_resume, resume):
    while True:
        prompt_resume = input ("Would you like to add another task? (Y/N): ").upper().strip()
        if prompt_resume == "Y" or prompt_resume == "YES":
            resume = True
            pass
        elif prompt_resume == "N" or prompt_resume == "NO":
            resume = False
            pass
        else:
            print("ERROR: Please Choose Y/N: ")
            continue
        return resume

while True:
    title, status = add_task(title,status)
    tasks[task_id] = {
        "title": title,
        "status": status
    }
    task_id += 1
    resume = start_stop(prompt_resume,resume)
    if resume == True:
        continue
    elif resume == False:
        break

print()

for task in tasks:
    print(tasks[task]["title"], "-", tasks[task]["status"])

print()

