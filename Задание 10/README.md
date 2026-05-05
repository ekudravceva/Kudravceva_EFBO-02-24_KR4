# Задание 10

## Установка
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
uvicorn app.main:app --reload
```

## Задание 10.1

### Проверка
- GET http://localhost:8000/items/1 — успешный запрос (200)
- GET http://localhost:8000/items/999 — CustomExceptionB (404)
- GET http://localhost:8000/check-value/5 — успешный запрос (200)
- GET http://localhost:8000/check-value/-5 — CustomExceptionA (400)

## Задание 10.2

### Проверка
(Удобнее всего тестировать через Swagger UI)

- POST http://localhost:8000/docs :

Успешный запрос:
```json
{
  "username": "testuser",
  "age": 25,
  "email": "test@example.com",
  "password": "12345678"
}
```

Ошибки валидации (422):
- возраст меньше 18
- короткий пароль (меньше 8 символов)
- длинный пароль (больше 16 символов)
- некорректный email
- отсутствует обязательное поле