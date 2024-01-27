


def view_all_tasks():
    print("Всі таски:")
    for i, task in enumerate(list_task):
        print(f"#{i + 1}: {task['title']}")