


def view_all_tasks():
    print("Всі таски:")
    for i, task in enumerate(tasks):
        print(f"#{i + 1}: {task['title']}")