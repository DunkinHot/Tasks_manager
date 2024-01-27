def view_tasks(some_task: [], task_index: int):
    if some_task is not None and some_task[task_index] is not None:
        task_name=some_task[task_index][0]
        task_description=some_task[task_index][1]
        task_date=some_task[task_index][2]
        print(f"Task name-> {task_name}, \nTask description-> {task_description}, \nTask date-> {task_date}")