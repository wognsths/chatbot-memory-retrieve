from fastapi import APIRouter, Depends
from src.chat.schemas import ChatRequest, ChatResponse
from src.chat.service import process_message, get_chat_history
from src.config.db_config import get_database

router = APIRouter()

@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await process_message(
        request.session_id, 
        request.message, 
        request.category
    )
    
    return ChatResponse(
        response=response,
        session_id=request.session_id
    )

@router.get("/{session_id}/history")
async def history(session_id: str):
    messages = await get_chat_history(session_id)
    return {"messages": messages}
