# courses

# Для запуску

1) Клонувати проект

2) запустити команду python3 -m pip install < requirements.txt

3) у папці з файлом manage.py запустити команду python3 -m manage makemigrations

4) запустити команду python3 -m manage migrate

5) запустити команду python3 -m manage runserver для запуску web проекту.

# Завдання

1) Додавання курсу в каталог <br/>
Форма додавання курсу в html або json форматах, на вибір, знаходиться внизу головної сторінки під списком усіх курсів

2) Відображення списку курсів <br/>
Список всіх курсів знаходиться на головній сторінці.

3) Відображення деталей курсу по id <br/>
Сторінка з деталями по курсу знаходиться по посилання атрибуту detail_url кожного курсу у списку

4) Пошук курсу за назвою і фільтр по датах <br/>
Форми пошуку та фільтрів з'являються по натисканню на кнопку 'Фільтри' головної сторінки

5) Зміна атрибутів курсу <br/>
Форма зміни атрибутів курсу знаходиться під детальною інформацією відповідного курсу на сторінці з деталями курсу

6) Видалення курсу <br/>
Видалення курсу з каталогу доступне по натисканню кнопки 'DELETE' та підтверження видалення на сторінці з деталями курсу

# Тести

Модульні тести доступні у модулі catalog/tests.py

# Адміністрація

Адміністративна панель доступна за шляхом <хост>:<порт>/admin/ <br/>
Для створення адміністратора потрібно виконати команду python3 -m manage createsuperuser та ввести дані адміністратора або зайти з під існуючого адміністратора: <br/>
Логін: admin, пароль: S1mplePassword
