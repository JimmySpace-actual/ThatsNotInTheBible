from flask import Flask, request
import requests
import os
import sys
import json


# Read the access token and group ID from arguments
ACCESS_TOKEN = sys.argv[1]
GROUP_ID = sys.argv[2]
BOT_ID = sys.argv[3]  # Directly assign the Bot ID from arguments

app = Flask(__name__)

def get_messages():
    """Fetch the latest messages from the group."""
    url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    params = {"token": ACCESS_TOKEN, "limit": 20}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        messages = response.json()["response"]["messages"]
        return messages
    else:
        print(f"Error fetching messages: {response.status_code} - {response.text}")
        return []

def send_message(text):
    """Send a message to the GroupMe group."""
    url = "https://api.groupme.com/v3/bots/post"
    data = {
        "bot_id": BOT_ID,
        "text": text
    }
    requests.post(url, json=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print(f"Received message: {data}")

    # Avoid responding to your own messages
    if data.get("sender_type") == "bot":
        return "OK", 200

    message_text = data.get("text", "").lower()

    # Test script: respond when "test" is in the message
    if "test" in message_text:
        send_message("Test successful!")
    
    return "OK", 200

if __name__ == "__main__":
    # Start ngrok tunnel on port 5000 and print the public URL
    
    # Run the Flask server
    app.run(port=5000)
