from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.product_review import ProductReview


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://root:rootroot@localhost:27017/productreviews?authSource=admin"
    )

    await init_beanie(database=client.db_name, document_models=[ProductReview])
