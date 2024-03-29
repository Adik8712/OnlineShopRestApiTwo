# Online Shop Rest API

Online Shop Rest API - это проект для онлайн магазина, который предоставляет RESTful API для управления пользователями, продуктами, заказами, доставкой и поддержкой.

## Описание проекта

Этот проект разделен на несколько приложений:

- **accounts**: Управление пользователями, включая аутентификацию, авторизацию и профили пользователей.
- **delivery**: Управление доставкой товаров.
- **markets**: Управление магазинами и продуктами.
- **support**: Управление службой поддержки для обработки запросов и обратной связи от пользователей.

## Установка

1. Склонируйте репозиторий на локальную машину:

```
git clone https://github.com/Adik8712/OnlineShopRestApiTwo.git
```

2. Создайте виртуальное окружение и активируйте его:

```
cd OnlineShopRestApi
virtualenv venv
source venv/bin/activate  # Для Unix/Mac
venv\Scripts\activate     # Для Windows
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Примените миграции:

```
python3 manage.py makemigrations
python manage.py migrate
```

5. Запустите сервер разработки:

```
python manage.py runserver
```

## Структура проекта

```
.
├── apps
│   ├── accounts
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── delivery
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── markets
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── support
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       ├── models.py
│       ├── signals.py
│       ├── tests.py
│       └── views.py
├── config.ini
├── create_project.md
├── db.sqlite3
├── LICENSE
├── manage.py
├── media
├── OnlineShopRestApi
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│    wsgi.py
├── plaintext.tree
├── push.sh
├── README.md
├── requirements.txt
└── static
```

## Сообщения

Любые вопросы или предложения по улучшению проекта приветствуются. Вы можете связаться с нами по электронной почте abashevadil87@gmail.com

## Лицензия

Этот проект лицензирован по лицензии [MIT](LICENSE).