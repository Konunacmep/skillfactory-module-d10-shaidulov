
Проект каталога автомобилей.
Для того, чтобы запустить проект:
1. необходимо подготовить виртуальное окружение для него командой 
python3 -m venv path
2. активировать окружение
source path\bin\activate
3. поместить в папку файлы проекта, перейти туда и запустить
pip install -r requirements.txt
4. Создать файл .env в директории проекта и прописать в нем значения для
SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
5. Применить миграции python3 manage.py migrate
6. Теперь можно запустить проект
python3 manage.py runserver
Для проверки работоспособности понадобится добавить в бд записи.
Для этого нужно создать суперузера python3 manage.py createsuperuser
и уже в админке добавлять все, что нужно.

В файле skillfactory содержится конфигурация nginx
