import asyncio
from app.database import async_session_maker
from app.models import Product

async def insert_products():
    async with async_session_maker() as session:
        products = [
            Product(title="Ручка", price=120, count=10),
            Product(title="Карандаш", price=80, count=25),
        ]
        session.add_all(products)
        await session.commit()
        print("Добавлены 2 продукта")

if __name__ == "__main__":
    asyncio.run(insert_products())