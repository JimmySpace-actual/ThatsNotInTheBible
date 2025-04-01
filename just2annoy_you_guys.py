import requests
import time
import sys
import os

# Replace these with your bot's info
ACCESS_TOKEN = sys.argv[1]  # Your GroupMe bot access token
GROUP_ID = sys.argv[2]  # The ID of your GroupMe group
# BOT_ID = sys.argv[3]  # Bot ID from command line argument
SENDER_ID = sys.argv[3]  # Sender ID from command line argument
MESSAGE = "it works"

def get_messages(after_id):
    """Fetch the latest messages from the GroupMe group using the bot."""
    url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    if after_id == None:
        params = {"token": ACCESS_TOKEN, "limit": 1}  # Get the last  messages
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()["response"]["messages"]
        else:
            print(f"Error fetching messages: {response.status_code} - {response.text}")
            return []
        
    params = {"token": ACCESS_TOKEN, "after_id": after_id}  # Get the last 20 messages
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["response"]["messages"]
    else:
        print(f"Error fetching messages: {response.status_code} - {response.text}")
        return []

def print_new_messages():
    """Poll GroupMe for new messages and print them."""
    after_id = None
    with open ("kjbibleUniqueCleaned.txt", "r") as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
        words = set(lines)
    while True:
        messages = get_messages(after_id)
        
        # Check for new messages
        if messages:
            for message in messages:
                # Only print new messages that were not seen before
                if after_id is not None and after_id == message["id"]:
                    continue
                after_id = message["id"]
                if message["sender_type"] == "bot":
                    continue
                print(f"New message: {message['text']} from {message['name']}")
                # message_words = message["text"].lower().split()
                # message_set = set(message_words)
                # for elem in message_set:
                #     print(elem)
                # print(message_set & words)
                # if message_set & words != set():
                #     continue
                    
                # else:
                    # Respond to the test message
                    # curl_command = f"curl -d '{"text" : "Your message here", "bot_id" : "e20619c8b4652348f8511c2349"}' https://api.groupme.com/v3/bots/post"
                    
                if message["sender_id"] == "80414071":
                    headers = {
                        # Already added when you pass json=
                        # 'Content-Type': 'application/json',
                    }

                    params = {
                        'token': ACCESS_TOKEN,
                    }

                    json_data = {
                        'message': {
                            'text': "Lawrence you should be asleep right now!",
                            'sender_id': SENDER_ID,
                        },
                    }

                    response = requests.post(f'https://api.groupme.com/v3/groups/{GROUP_ID}/messages', params=params, headers=headers, json=json_data)

                        
                        # os.system(curl_command)

        time.sleep(1)  # Poll every 1 seconds

if __name__ == "__main__":
    print_new_messages()