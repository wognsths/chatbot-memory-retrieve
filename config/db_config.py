from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase

class Database:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

db = Database()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient("mongodb://localhost:27017")
    db.db = db.client.chatbot_db

async def close_mongo_connection():
    if db.client:
        db.client.close()

def get_database() -> AsyncIOMotorDatabase:
    return db.db