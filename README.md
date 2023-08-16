# Bookmarks API Service
Сервис для хранения закладок с различной информацией о странице - собранной либо из Open Graph либо из обычных meta тегов. Пользователи могут регистрироваться, создавать коллекции, добавлять закладки в коллекции. Одна и та же закладка может быть в одной или нескольких коллекциях сразу. Либо быть без коллекции.

## По проблемам и вопросам запуска писать на https://t.me/lordsanchez
### Как запустить проект:

Клонировать репозиторий:

```
git clone https://github.com/FFFSanchez/marksbook-api.git
```

Cоздать и активировать виртуальное окружение, установить зависимости:

```
python -m venv env

source venv/Scripts/activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

Добавить свой файл .env в главную папку marksbook, пример файла:

```
SECRET_KEY=django-insecure-($vi^cu)cp=ot8e5a%*x#nv3ifv&+vlol32xji)(xa+qn!#9i*

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres

DB_HOST=pgdb
DB_PORT=5432

```

Запуск через docker compose:

```
находясь в одной папке с docker-compose.yml

docker-compose up --build -d
docker-compose run backend python manage.py migrate
docker-compose run backend python manage.py collectstatic
docker-compose run backend cp -r /app/collected_static/. /app/static_bm_backend/static/
```

Готово, сервис запущен и доступен по адресам 
+ http://localhost:8000/api/v1/
+ http://localhost:8000/admin/
+ http://localhost:8000/api/auth/

Документация к эндпоинтам доступна по адресу http://localhost:8000/swagger/

## Описание функциональности
Основные функции сервиса:
- Регистрация пользователя (по email и паролю) (`http://localhost:8000/api/auth/users/`)
- Логин пользователя по логину и паролю с выдачей Token (`http://localhost:8000/api/auth/token/login/`)
  - После получения Токена для дальнейших действий нужно добавлять его в заголовок запроса Token ...
- Логаут пользователя по логину и паролю с удалением Token (`http://localhost:8000/api/auth/token/logout/`)
- Создание закладки с указанием URL страницы (`http://localhost:8000/api/v1/bookmarks/`)
  - при сохранении закладки производится считывание заголовка страницы, описание, тип страницы, картинка
  - при сохранении закладки есть возможность указать коллекцию
- Создание коллекции (`http://localhost:8000/api/v1/collections/`)


