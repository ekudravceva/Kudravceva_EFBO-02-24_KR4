# Задание 10.1

### Установка
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Запуск
```bash
uvicorn app.main:app --reload
```

### Проверка
- GET http://localhost:8000/items/1 — успешный запрос (200)
- GET http://localhost:8000/items/999 — CustomExceptionB (404)
- GET http://localhost:8000/check-value/5 — успешный запрос (200)
- GET http://localhost:8000/check-value/-5 — CustomExceptionA (400)