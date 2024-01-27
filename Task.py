from datetime import datetime as dtdt

list_task = []

def add_task(name_task, descripion_task, date_task, deadline_task):
    list_task.append([name_task, descripion_task, date_task, deadline_task])
    date_task = dtdt(year=int(input("Year= ")),month=int(input("Month= ")),day=int(input("Day= ")))
    return "Таску додано", list_task

    
    




def view_all_tasks():
    print("Всі таски:")
    for i, task in enumerate(list_task):
        print(f"#{i + 1}: {task['title']}")


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
