# Задание 9.1

## Установка
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
```
## Запуск

```bash
# Применить миграции
alembic upgrade head

# Добавить тестовые данные
python3 -m app.insert_data

# Запустить приложение
uvicorn app.main:app --reload
```

## Проверка
GET http://localhost:8000/products - список продуктов

GET http://localhost:8000/check-schema - структура таблицы

## Команды Alembic
alembic revision --autogenerate -m "описание" - создать миграцию

alembic upgrade head - применить все миграции

alembic downgrade -1 - откатить последнюю

alembic current - текущая версия

alembic history - история миграций