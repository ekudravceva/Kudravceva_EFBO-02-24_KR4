from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Задание 10.1")

# Пользовательские исключения
class CustomExceptionA(Exception):
    def __init__(self, detail: str = "Не выполнено условие"):
        self.detail = detail
        self.status_code = 400

class CustomExceptionB(Exception):
    def __init__(self, detail: str = "Ресурс не найден"):
        self.detail = detail
        self.status_code = 404

# Модель ответа с ошибкой
class ErrorResponse(BaseModel):
    status_code: int
    message: str
    type: str

# Обработчики исключений
@app.exception_handler(CustomExceptionA)
async def custom_a_handler(request: Request, exc: CustomExceptionA):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            status_code=exc.status_code,
            message=exc.detail,
            type="CustomExceptionA"
        ).model_dump()
    )

@app.exception_handler(CustomExceptionB)
async def custom_b_handler(request: Request, exc: CustomExceptionB):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            status_code=exc.status_code,
            message=exc.detail,
            type="CustomExceptionB"
        ).model_dump()
    )

items = {1: "Товар 1", 2: "Товар 2"}

# Эндпоинты
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in items:
        raise CustomExceptionB(detail=f"Товар с id {item_id} не найден")
    return {"id": item_id, "name": items[item_id]}

@app.get("/check-value/{value}")
async def check_value(value: float):
    if value < 0:
        raise CustomExceptionA(detail=f"Значение {value} меньше нуля")
    return {"value": value, "status": "ok"}