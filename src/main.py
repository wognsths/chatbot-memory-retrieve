from fastapi import FastAPI
from src.chat.router import router as chat_router
from src.memory.router import router as memory_router

app = FastAPI(title="Chatbot API")

app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(memory_router, prefix="/memory", tags=["memory"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)