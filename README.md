# Проект cоциальная сеть YaTube API
### Описание
YaTube API представляет собой проект социальной сети в которой реализованы следующие возможности: 
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.
### Технологии
Python 3.7, Django 3.2, DRF, JWT + Djoser
### Запуск проекта в dev-режиме
- Клонировать репозиторий и перейти в него в командной строке.
Cоздать и активировать виртуальное окружение:
```bash
python -m venv env
source env/bin/activate
```
- Затем нужно установить все зависимости из файла requirements.txt
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполняем миграции:
```bash
python manage.py migrate
```
Создаем суперпользователя:
```bash
python manage.py createsuperuser
```
Запускаем проект:
```bash
python manage.py runserver
```
### Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна только в режиме чтения.
```bash
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
### Примеры работы с API для авторизованных пользователей
Для создания публикации используем:
```bash
POST /api/v1/posts/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Обновление публикации:
```bash
PUT /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```bash
PATCH /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```bash
DEL /api/v1/posts/{id}/
```
Получение доступа к эндпоинту /api/v1/follow/
(подписки) доступен только для авторизованных пользователей.
```bash
GET /api/v1/follow/ - подписка пользователя от имени которого сделан запрос
на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
- Авторизованные пользователи могут создавать посты,
комментировать их и подписываться на других пользователей.
- Пользователи могут изменять(удалять) контент, автором которого они являются.

### Добавить группу в проект нужно через админ панель Django:
```bash
admin/ - после авторизации, переходим в раздел Groups и создаем группы
```
Доступ авторизованным пользователем доступен по JWT-токену (Joser),
который можно получить выполнив POST запрос по адресу:
```bash
POST /api/v1/jwt/create/
```
Передав в body данные пользователя (например в postman):
```bash
{
"username": "string",
"password": "string"
}
```
Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:
```bash
Authorization: Bearer {your_token}
```
Обновить JWT-токен:
```bash
POST /api/v1/jwt/refresh/ - обновление JWT-токена
```
Проверить JWT-токен:
```bash
POST /api/v1/jwt/verify/ - проверка JWT-токена
```
### Примеры запросов

Создаем новый пост
Передаем POST-запрос, в заголовке указываем Authorization:Bearer <токен>
```bash
POST .../api/v1/posts/
```
Обязательное поле: text
{ "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится." }

Пример ответа:

{ "id": 14, "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.", "author": "anton", "image": null, "group": 1, "pub_date": "2022-07-19T16:04:56.154976Z"}

Пример GET-запроса с токеном: получаем информацию о группе. 
```bash
GET .../api/v1/groups/2/
```

Пример ответа:

{ "id": 2, "title": "Художники", "slug": "painter", "description": "Посты на тему художников" }
