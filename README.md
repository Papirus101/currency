**Курс валют**
Инструкция по развёртыванию сервера:
1. Установить все зависимости из файла requirements.txt `pip install -r requirements.txt`
2. Запустить postgresql `docker-compose up -d`
3. Выполнить миграции `python manage.py migrate`
4. Для обновления информации о курсах валют, запустить файл parsecurrency.py `python parsecurrency.py`
5. Запустить сервер командой `python manage.py runserver`