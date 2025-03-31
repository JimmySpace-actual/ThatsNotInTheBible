import requests
import time
import sys
import os

# Replace these with your user info
ACCESS_TOKEN = sys.argv[1]  # Your personal GroupMe OAuth access token
GROUP_ID = sys.argv[2]  # The ID of your GroupMe group

def get_messages():
    """Fetch the latest messages from the GroupMe group using your personal account."""
    url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    params = {"token": ACCESS_TOKEN, "limit": 1}  # Get the last 1 message
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["response"]["messages"]
    else:
        print(f"Error fetching messages: {response.status_code} - {response.text}")
        return []

def send_message(text):
    """Send a message to the GroupMe group from your personal account."""
    url = "https://api.groupme.com/v3/messages"
    data = {
        "text": text,
        "group_id": GROUP_ID,
        "token": ACCESS_TOKEN
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"Sent message: {text}")
    else:
        print(f"Error sending message: {response.status_code} - {response.text}")

def print_new_messages():
    """Poll GroupMe for new messages and print them."""
    last_checked_message_id = None

    while True:
        messages = get_messages()
        
        # Check for new messages
        if messages:
            for message in messages:
                # Only print new messages that were not seen before
                if last_checked_message_id is None or message["id"] != last_checked_message_id:
                    print(f"New message: {message['text']} from {message['name']}")
                    last_checked_message_id = message["id"]

                    # Respond to the test message (e.g., if message contains "test")
                    if "test" in message["text"].lower():
                        send_message("Your message here")  # Replace with your desired response

                if "test" in message["text"].lower():
                    headers = {
                        # Already added when you pass json=
                        # 'Content-Type': 'application/json',
                    }

                    params = {
                        'token': 'mRUpT79aaWG9pHwh0PHsmFfQRGs98cf4Pjx5U8if',
                    }

                    json_data = {
                        'message': {
                            'text': 'GET ME A MONSTER',
                            'sender_id': '92013354',
                        },
                    }

                    response = requests.post('https://api.groupme.com/v3/groups/106874570/messages', params=params, headers=headers, json=json_data)

        time.sleep(1)  # Poll every second (adjust as needed)

if __name__ == "__main__":
    print_new_messages()
