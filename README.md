### Тестовое задание

## API для получения объявлений

Реализовван API на Django framework для получения данных объявлений.

## Для запуска проекта

# Создать выртуальное окружение

python -m venv venv

source venv/Scripts/activate

# Установить зависимости:

pip install -r requirements.txt

# Создать .env
Пример заполненного файла
DJANGO_SECRET_KEY='my-secret-django-key'
DEBUG=TRUE

# Сделать миграции
cd ads/
python manage.py migrate

# Создать суперпользователя

python manage.py createsuperuser

# Загрузить данные объявлений

python manage.py load_ads

# Тестовые запросы через Postman

Получаем токен через POST запрос на http://127.0.0.1:8000/api/token/:
{
    "email": "your-admin-email@admin.ru",
    "password": "your-admin-password",
}

Пример GET запроса:
В headers передаем access token
Key: Authorization
Value: Bearer YOUR_ACCESS_TOKEN
http://127.0.0.1:8000/api/ads/97431277/

Пример вывода:
{
    "title": "Монтаж видеонаблюдения Hikvision HiWatch Trassir, СКУД, домофонов",
    "ad_id": 97431277,
    "author": "doneit",
    "views": 491,
    "position": 2
}
