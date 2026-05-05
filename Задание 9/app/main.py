from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from app.database import get_db
from app.models import Product

app = FastAPI(title="Задание 9.1")

@app.get("/")
async def root():
    return {"message": "Миграции Alembic работают"}

@app.get("/products")
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products

@app.get("/check-schema")
async def check_schema(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("PRAGMA table_info(products)"))
    columns = result.fetchall()
    return {"columns": [{"name": col[1], "type": col[2], "notnull": col[3]} for col in columns]}