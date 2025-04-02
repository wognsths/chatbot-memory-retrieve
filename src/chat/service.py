from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import MongoDBChatMessageHistory
from src.config.db_config import get_database

# Store for chat histories
message_histories = {}

def get_session_history(session_id: str):
    if session_id not in message_histories:
        message_histories[session_id] = MongoDBChatMessageHistory(
            connection_string="mongodb://localhost:27017",
            database_name="chatbot_db",
            collection_name="chat_histories",
            session_id=session_id
        )
    return message_histories[session_id]

def create_chain():
    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    chain = prompt | llm
    return RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history"
    )

async def process_message(session_id: str, message: str, category: str):
    db = get_database()
    
    # Log conversation metadata
    await db.conversation_metadata.update_one(
        {"session_id": session_id},
        {
            "$set": {
                "last_updated": datetime.now(),
                "category": category
            },
            "$setOnInsert": {"created_at": datetime.now()}
        },
        upsert=True
    )
    
    # Process the message with LLM
    chain = create_chain()
    response = chain.invoke(
        {"input": message},
        config={"configurable": {"session_id": session_id}}
    )
    
    return response.content

async def get_chat_history(session_id: str):
    history = get_session_history(session_id)
    return history.messages
