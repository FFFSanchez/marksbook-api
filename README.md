# Bookmarks API Service
Сервис для хранения закладок с сохранением информациии о странице собранной либо из Open Graph либо из обычных meta тегов. Пользователи могут регистрироваться, создавать коллекции, добавлять закладки в коллекции. Одна и та же закладка может быть в одной или нескольких коллекциях сразу. Либо быть без коллекции.

### Стек
+ Django DRF
+ PostgreSQL
+ Docker compose
+ Nginx
+ WSL
+ GitHub
+ BS4
+ Postman

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

Готово, сервис запущен и доступен на localhost:8000 

Документация к эндпоинтам доступна по адресу http://localhost:8000/swagger/

## Описание функциональности

Основные функции сервиса:
- Зарегистрироваться. Регистрация по email и паролю (POST `http://localhost:8000/api/auth/users/`)
- Логин пользователя по логину и паролю с выдачей Token (POST `http://localhost:8000/api/auth/token/login/`)
  - После получения Токена для дальнейших действий нужно добавлять его в заголовок запроса Token ...
- Логаут пользователя по логину и паролю с удалением Token (POST `http://localhost:8000/api/auth/token/logout/`)
- Добавить закладку с указанием URL страницы (POST `http://localhost:8000/api/v1/bookmarks/`)
  - при сохранении закладки производится считывание:
    - Заголовок страницы
    - Краткое описание
    - Ссылка на страницу
    - Тип ссылки. У нас их будет пока что 5 (website, book. article, music, video), по умолчанию используем тип website
    - Картинка превью берется из поля og:image
    - Дата и время создания
    - Дата и время изменения
  - при сохранении закладки есть возможность указать коллекцию
  - добавить в коллекцию можно позже PATCH запросом на ендпоинт конкретной заклдаки (`http://localhost:8000/api/v1/bookmarks/<id>/`)
- Создание коллекции (POST `http://localhost:8000/api/v1/collections/`)
  - Название
  - Краткое описание
  - Дата и время создания
  - Дата и время изменения
- Удалить коллекцию(Удаляется только коллекция, закладки остаются у пользователя)(DELETE `http://localhost:8000/api/v1/collections/<id>/`)
- Поменять название/описание коллекции (PATCH `http://localhost:8000/api/v1/collections/<id>/`)
Так же доступны все возможные действия со своим аккаунтом, т.к. используется djoser - все ендпоинты прописаны в Swagger


#### CI/CD через github workflow в процессе настройки

### Автор: Александр Трифонов
