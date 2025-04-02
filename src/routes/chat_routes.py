from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.services.memory_manager import store_conversation, retrieve_conversation

app = FastAPI()

class ConversationData(BaseModel):
    user_id: str
    conversation: str
    category: str

@app.post("/store_conversation")
async def store(data: ConversationData):
    await store_conversation(data.user_id, data.conversation, data.category)
    return {"message": "Conversation stored successfully"}

@app.get("/retrieve_conversation")
async def retrieve(user_id: str, category: str):
    conversations = await retrieve_conversation(user_id, category)
    if not conversations:
        raise HTTPException(status_code=404, detail="No conversations found")
    return conversations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
