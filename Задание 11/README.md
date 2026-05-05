# Задание 11( 11.1, 11.2)
## Модульные и асинхронные тесты FastAPI

### Установка
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Запуск приложения
```bash
uvicorn app.main:app --reload
```

### Запуск синхронных тестов (Задание 11.1)
```bash
pytest test/test_sync.py -v
```

### Запуск асинхронных тестов (Задание 11.2)
```bash
pytest test/test_async.py -v
```

### Запуск всех тестов
```bash
pytest -v
```