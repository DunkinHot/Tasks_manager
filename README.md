Project: Менеджер завданнь (тім_лід Віталій Галецький

Опис:
Створіть простий таск-менеджер, який дозволить користувачам додавати, переглядати та редагувати таски. Для цього проекту потрібно застосувати: функції, цикли, умовні оператори, модулі datetime, re та math.
Умови виконання:

1) Створення таски: (Іл'я Іванов)
   
Створіть функцію add_task яка буде приймати деталі таски (такі як назву таски, опис таски, дату додавання та дату виконання) та додавати таски до списку.
Валідуйте формат введенної дати на співпадіння або з 2024-01-25 або з 25-01-2024.

3) Виведення інформації про таску:
   
Створіть функцію view_tasks яка буде виводити одну таску по індексу у форматованому вигляді.
Потрібно вивести: назву, опис та дату виконання таски.

5) Виведення інформації про всі таски: (Віталій Кохан)
Створіть функцію view_all_tasks яка буде виводити усі таски у вигляді таблиці.
Потрібно вивести: назву, опис та дату виконання таски.

6) Зміна статусу на виконаний:
Напишіть функцію mark_completed яка буде позначати таску як виконану.
Та напишіть функцію view_all_completed_tasks яка буде виводити окремо усі виконані таски.

7) Зміна статусу на в процесі:
Напишіть функцію mark_in_progress яка буде позначати таску як в процесі виконання.
Та напишіть функцію view_all_in_progress_tasks яка буде виводити окремо усі виконані таски.

8) Перевірка дедлайну таски: (Aleksandr Atanasov)
Створіть функцію check_overdue яка знаходить усі таски, які перейшли за дедлайн.

9) Пріоритет тасок:
Додайте пріоритет до кожної таски (Високий, Середній, Низький)
Напишіть функцію, яка виводить усі таски з Високим пріоритетом
Напишіть функцію, яка виводить усі таски з Середнім пріоритетом
Напишіть функцію, яка виводить усі таски з Низьким пріоритетом

10) Видалення тасок:
Дайте можливість видалити таски по назві.

11) Кількість тасок:
Напишіть функцію, яка буде рахувати загальну кількість тасок.
Напишіть функцію, яка буде рахувати кількість виконаних тасок.
Напишіть функцію, яка буде рахувати кількість не виконаних тасок.

12) Сортування тасок:
Напишіть функцію, яка буде сортувати таски за датою виконання.
Напишіть функцію, яка буде сортувати таски за датою додавання.

11)Пошук тасок:
Напишіть функцію search_tasks яка буде шукати по слову у назві або описі таски.
Напишіть функцію search_tasks_by_date яка буде знаходити усі таски, в яких дата створення дорівнює переданій.

12) Статистика тасок:
Напишіть функцію, яка буде рахувати статистику тасок, таку як відсоток закінчених тасок, відсоток тасок в процесі та середній пріоритет тасок.

13) Додаткови умови*:
Обробка введення користувача:
Напишіть функцію, яка буде в нескінченному циклі обробляти команди користувача.
Введення команд потрібно робити за допомогою функції input.
Команда add <назва_таски> <опис_таски> <дата_виконання> має додавати нову таску і виводити повідомлення про успішне збередення.
