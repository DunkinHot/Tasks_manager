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

