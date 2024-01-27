

from datetime import datetime as dtdt

list_task = []

def add_task(name_task, descripion_task, date_task, deadline_task):
    list_task.append([name_task, descripion_task, date_task, deadline_task])
    date_task = dtdt(year=int(input("Year= ")),month=int(input("Month= ")),day=int(input("Day= ")))
    return "Таску додано", list_task

#Task 2
def view_tasks(some_task: [], task_index: int):
    if some_task is not None and some_task[task_index] is not None:
        task_name=some_task[task_index][0]
        task_description=some_task[task_index][1]
        task_date=some_task[task_index][2]
        print(f"Task name-> {task_name}, \nTask description-> {task_description}, \nTask date-> {task_date}") 

#Task 3
def view_all_tasks():
    print("Всі таски:")
    for i, task in enumerate(list_task):
        print(f"#{i + 1}: {task['title']}")

#Task 4
def mark_completed(name_task):
    for task in list_task:
        if task[0] == name_task:
            task.append('Done')
    return 'Task_completed'

def view_all_completed_tasks():
    task_completed=[]
    for task in list_task:
        if task[4]=='Done':
            task_completed.append(task)
    return 'All_completed_tasks', task_completed

#Task 5
def mark_in_progress(name_task):
    for task in list_task:
        if task[0] == name_task:
            task.append('in_progress')
    return 'in_progress'

def view_all_in_progress_tasks():
    task_in_progress=[]
    for task in list_task:
        if task[4]=='in_progress':
            task_in_progress.append(task)
    return 'in_progress', task_in_progress



#________________


# eight_task Видалення тасок: Дайте можливість видалити таски по назві.
def delete_task_by_name(all_tasks: [], task_name: str):
    if all_tasks is not None:
        task_number=0
        for task in all_tasks:
            if task is not None and task_name is not None and task[0]==task_name:
                deleted_task=all_tasks.pop(task_number)
                print(f"Next task was successfully deleted ->")
                print(f"- task name: {deleted_task[0]}, \n - task description: {deleted_task[1]}, \n - date task: {deleted_task[2]}, \n - task deadline: {deleted_task[3]}")
            task_number+=1

