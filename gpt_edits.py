import requests
import time
import sys
import os
import random

# Replace these with your bot's info
ACCESS_TOKEN = sys.argv[1]
GROUP_ID = sys.argv[2]
SENDER_ID = sys.argv[3]

def get_messages(after_id):
    """Fetch the latest messages from the GroupMe group using the bot."""
    url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    params = {"token": ACCESS_TOKEN}
    if after_id:
        params["after_id"] = after_id
    else:
        params["limit"] = 20  # Initial fetch

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["response"]["messages"]
    else:
        print(f"Error fetching messages: {response.status_code} - {response.text}")
        return []

def send_message(text, sender_name, sender_id):
    """Send a message to the GroupMe group with an @ mention."""
    full_text = f"@{sender_name} {text}"
    print(f"Sending message: {full_text}")
    params = {'token': ACCESS_TOKEN}
    json_data = {
        'message': {
            'text': full_text,
            'attachments': [
                {
                    'type': 'mentions',
                    'user_ids': [sender_id],
                    'loci': [[0, len(sender_name) + 1]]
                }
            ],
            'sender_id': SENDER_ID
        }
    }
    response = requests.post(
        f'https://api.groupme.com/v3/groups/{GROUP_ID}/messages',
        params=params,
        json=json_data
    )
    if response.status_code != 201:
        print(f"Error sending message: {response.status_code} - {response.text}")

def print_new_messages():
    after_id = None
    with open("kjbibleUniqueCleaned.txt", "r") as file:
        bible_words = set(line.strip().lower() for line in file)

    # Track the most recent message at start without skipping responses forever
    initial_messages = get_messages(None)
    if initial_messages:
        after_id = initial_messages[0]["id"]

    seen_ids = set()

    while True:
        messages = get_messages(after_id)

        if messages:
            for message in messages:
                if message["id"] in seen_ids:
                    continue

                seen_ids.add(message["id"])
                after_id = message["id"]

                # Skip messages sent by this bot itself using sender_id
                if message.get("sender_id") == SENDER_ID:
                    continue

                text = message.get("text", "")
                attachments = message.get("attachments", [])
                sender_name = message.get("name", "Unknown")
                sender_id = message.get("sender_id")

                print(f"New message: {text} from {sender_name}")
                message_words = text.lower().split()

                # Skip short messages
                if len(message_words) < 3:
                    continue

                message_set = set(message_words)

                if message_set & bible_words:
                    impurity = 100 * ((len(message_set) - len(message_set & bible_words)) / len(message_set))

                    if impurity == 0:
                        send_message("You are a pure soul, a holy spirit, a bright beacon of light in this hellish abyss, the only Saint to be found in this land of Sinners. The Gates of Heaven are open to you and you alone, welcome to My Kingdom child.", sender_name, sender_id)
                    else:
                        send_message(f"Your thoughts are {impurity:.1f}% impure", sender_name, sender_id)

                elif not text.strip() and attachments:
                    image_urls = [
                        "https://en.wikipedia.org/wiki/File:Buddy_christ.jpg",
                        "https://curious-archive.b-cdn.net/wp-content/uploads/danilo-wolf-angel-23-1024x644.jpg",
                        "https://static1.squarespace.com/static/610e8a1442e2e073cafbc00f/6110f5866397ce460361d3dd/63f5e0e59c152d5aa7dca368/1677480227546/1505490457119557293.jpg?format=1500w",
                        "https://i.pinimg.com/474x/38/9d/5f/389d5f3ac9f92038c261602c13d82d88.jpg",
                        "https://gregatkinson.com/wp-content/uploads/2013/06/loser-600x450.jpg",
                        "https://eyestoseetherevelation.com/wp-content/uploads/2022/12/EDHH93-1280x640.jpg",
                        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZhOBCe0Sc0hkm36i0QqyznzJ7LwjTTKEawujCQDcIZQzg2nred260UMzrjp1Dt7gQCMMlO3bNZ_LJVoCxHPruET0Z4DvnEN3acA8ZcStSlxreLsVZFc0LIUkdbEyZTNTCsfkZdJuY-rY/s400/Jesus-Christ-Limpias-Spain.jpg"
                    ]
                    image_url = random.choice(image_urls)
                    send_message(f"[image] {image_url}", sender_name, sender_id)

                else:
                    send_message("NONE of these words are in The Bible, you are going straight to Hell", sender_name, sender_id)

        time.sleep(1)

if __name__ == "__main__":
    print_new_messages()

