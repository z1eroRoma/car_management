# car_management

Клонируйте репозиторий:
git clone https://github.com/z1eroRoma/car_management.git
cd car_management

Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # для Unix/MacOS
venv\Scripts\activate  # для Windows

Установите зависимости:
pip install -r requirements.txt

Выполните миграции базы данных:
python manage.py migrate

Создайте суперпользователя для доступа к административной панели:
python manage.py createsuperuser

Запустите сервер разработки:
python manage.py runserver

Откройте браузер и перейдите по адресу:
http://127.0.0.1:8000/




Использование API
Автомобили
Получение списка автомобилей:
GET /api/cars/

Получение информации о конкретном автомобиле:
GET /api/cars/<id>/

Создание нового автомобиля:
POST /api/cars/

Обновление информации о автомобиле:
PUT /api/cars/<id>/

Удаление автомобиля:
DELETE /api/cars/<id>/

Комментарии
Получение комментариев к автомобилю:
GET /api/cars/<id>/comments/

Добавление нового комментария к автомобилю:
POST /api/cars/<id>/comments/

Административная панель
Для доступа к административной панели перейдите по адресу:
http://127.0.0.1:8000/admin/
