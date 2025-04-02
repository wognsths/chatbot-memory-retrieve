from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    session_id: str
    message: str
    category: Optional[str] = "general"

class ChatResponse(BaseModel):
    response: str
    session_id: str

class ChatHistory(BaseModel):
    session_id: str
    messages: List[Message]
    category: str
    created_at: datetime
    updated_at: datetime
