from config.db_config import get_database
from datetime import datetime

async def store_conversation(user_id: str, conversation: str, category: str):
    db = await get_database()
    conversations_collection = db.conversations
    conversation_data = {
        "user_id": user_id,
        "category": category,
        "conversation": conversation,
        "timestamp": datetime.now()
    }
    await conversations_collection.insert_one(conversation_data)

async def retrieve_conversation(user_id: str, category: str):
    db = await get_database()
    conversations_collection = db.conversations
    query = {"user_id": user_id, "category": category}
    cursor = conversations_collection.find(query)
    return await cursor.to_list(length=None)
