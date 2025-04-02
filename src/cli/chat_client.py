import requests
import uuid
import sys

def main():
    session_id = str(uuid.uuid4())
    print(f"Starting new chat session: {session_id}")
    print("Type 'exit' to end the conversation")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == "exit":
            print("Conversation ended.")
            break
        
        # Send request to API
        response = requests.post(
            "http://localhost:8000/chat",
            json={
                "session_id": session_id,
                "message": user_input
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nAssistant: {data['response']}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    main()
