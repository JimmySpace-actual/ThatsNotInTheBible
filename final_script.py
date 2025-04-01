import requests
import time
import sys
import os
import random

# Replace these with your bot's info
ACCESS_TOKEN = sys.argv[1]  # Your GroupMe bot access token
GROUP_ID = sys.argv[2]  # The ID of your GroupMe group
# BOT_ID = sys.argv[3]  # Bot ID from command line argument
SENDER_ID = 0#sys.argv[3]  # Sender ID from command line argument
MESSAGE = "NONE of these words are in The Bible. Let my Light into your life or you will be going to Hell"

def get_messages(after_id):
    """Fetch the latest messages from the GroupMe group using the bot."""
    url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    if after_id == None:
        params = {"token": ACCESS_TOKEN, "limit": 20}  # Get the last  messages
        response = requests.get(url, params=params)
        if response.status_code == 200:
            message_temps = response.json()["response"]["messages"]
            print(type(message_temp))
            for message_temp in message_temps:
                print(message_temp['user_id'])
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
                message_words = message["text"].lower().split()
                message_set = set(message_words)
                #for elem in message_set:
                    #print(elem)
                #print(message_set & words)
                sender = messages["name"] #name of the person who sent the last message so that they can be specifically called out by God
                if message_set & words != set():
                    impurity = 100 * ((len(message_set) - (len(message_set & words))) / (len(message_set)))

                    if impurity == 0:
                        headers = {
                            # Already added when you pass json=
                            # 'Content-Type': 'application/json',
                        }

                        params = {
                            'token' : ACCESS_TOKEN,
                        }

                        json_data = {
                            'message' : {
                                'text' :f'@{sender} You are a pure soul, a holy spirit, a beacon of My Light in the dark depths of this Hell',
                                'sender_id' : SENDER_ID
                            },
                        }

                        response = requests.post(f'https://api.groupme.com/v3/groups/{GROUP_ID}/messages', params=params, headers=headers, json=json_data)

                    headers = {
                        # Already added when you pass json=
                        # 'Content-Type': 'application/json',
                    }

                    params = {
                        'token': ACCESS_TOKEN,
                    }

                    json_data = {
                        'message': {
                            'text': f'@{sender} Your thoughts are {impurity}% impure',
                            'sender_id': SENDER_ID,
                        },
                    }

                    response = requests.post(f'https://api.groupme.com/v3/groups/{GROUP_ID}/messages', params=params, headers=headers, json=json_data)


                #pretty sure for the line of code before I either want "" or "[]". It's definitely one of the two based on reading of the storage file
                elif message_set == set() and messages["attachments"] != "[]": #idk if I'm reading the attachments correctly, but the idea here is if someone sends an image or video without text we respond with an image
                #maybe randint this, have like 15 photos at the ready or something and respond with a random one. but for now I'm just gonna go with buddy jesus
                #currently can't tell how to process the image, I found something which lets me send a link to groupme in the post request but idk if I formatted that right and I also found something to have the
                #image as an opened file here that gets sent to groupme. RN this code does both which I think is DEFINITELY wrong. The post request is spitting out errors I know that much
                    rando = random.randint(0,5)
                    if rando == 0:
                        headers = {
                            'X-Access-Token': os.getenv(ACCESS_TOKEN, ''),
                            'Content-Type': 'image/jpeg'
                        }

                        with open('Buddy_christ.jpg', 'rb') as f:
                            data = f.read()

                        params = {
                                'token': ACCESS_TOKEN,
                            }
                    
                        json_data = {
                                'message': {
                                    'text': f'@{sender}',
                                    'sender_id': SENDER_ID
                            },
                        }
                        #I can't find a god damn thing online about sending a message and attachment at the same time, so uhhhhhh here's a guess at doing that
                        #the line below was ripped from a git repo and in the example line the 'inset your image url here' is in these <> brackets and I can't tell if that's to point it out or if its necessary
                        #response = requests.post(https://image.groupme.com/pictures?url=<https://en.wikipedia.org/wiki/File:Buddy_christ.jpg>, headers=headers, data=data, json=json_data, params=params)

                    elif rando == 1:
                        #https://curious-archive.b-cdn.net/wp-content/uploads/danilo-wolf-angel-23-1024x644.jpg
                        headers = {
                            'X-Access-Token': os.getenv(ACCESS_TOKEN, ''),
                            'Content-Type': 'image/jpeg'
                        }

                        params = {
                                'token': ACCESS_TOKEN,
                            }
                    
                        json_data = {
                                'message': {
                                    'text': f'@{sender}',
                                    'sender_id': SENDER_ID
                            },
                        }
                        #response = requests.post(https://image.groupme.com/pictures?url=<https://curious-archive.b-cdn.net/wp-content/uploads/danilo-wolf-angel-23-1024x644.jpg>, headers=headers, json=json_data, params=params)
                        continue

                    elif rando == 2:
                        #https://static1.squarespace.com/static/610e8a1442e2e073cafbc00f/6110f5866397ce460361d3dd/63f5e0e59c152d5aa7dca368/1677480227546/1505490457119557293.jpg?format=1500w
                        headers = {
                            'X-Access-Token': os.getenv(ACCESS_TOKEN, ''),
                            'Content-Type': 'image/jpeg'
                        }

                        params = {
                                'token': ACCESS_TOKEN,
                            }
                    
                        json_data = {
                                'message': {
                                    'text': f'@{sender}',
                                    'sender_id': SENDER_ID
                            },
                        }
                        #response = requests.post(https://image.groupme.com/pictures?url=<https://static1.squarespace.com/static/610e8a1442e2e073cafbc00f/6110f5866397ce460361d3dd/63f5e0e59c152d5aa7dca368/1677480227546/1505490457119557293.jpg?format=1500w>, headers=headers, json=json_data, params=params)
                        continue

                    elif rando == 3:
                        #https://i.pinimg.com/474x/38/9d/5f/389d5f3ac9f92038c261602c13d82d88.jpg
                        headers = {
                            'X-Access-Token': os.getenv(ACCESS_TOKEN, ''),
                            'Content-Type': 'image/jpeg'
                        }

                        params = {
                                'token': ACCESS_TOKEN,
                            }
                    
                        json_data = {
                                'message': {
                                    'text': f'@{sender}',
                                    'sender_id': SENDER_ID
                            },
                        }
                        #response = requests.post(https://image.groupme.com/pictures?url=<https://i.pinimg.com/474x/38/9d/5f/389d5f3ac9f92038c261602c13d82d88.jpg>, headers=headers, json=json_data, params=params)
                        continue

                    elif rando == 4:
                        #https://gregatkinson.com/wp-content/uploads/2013/06/loser-600x450.jpg
                        headers = {
                            'X-Access-Token': os.getenv(ACCESS_TOKEN, ''),
                            'Content-Type': 'image/jpeg'
                        }

                        params = {
                                'token': ACCESS_TOKEN,
                            }
                    
                        json_data = {
                                'message': {
                                    'text': f'@{sender}',
                                    'sender_id': SENDER_ID
                            },
                        }
                        #response = requests.post(https://image.groupme.com/pictures?url=<https://gregatkinson.com/wp-content/uploads/2013/06/loser-600x450.jpg>, headers=headers, json=json_data, params=params)
                        continue

                    elif rando == 5:
                        #https://eyestoseetherevelation.com/wp-content/uploads/2022/12/EDHH93-1280x640.jpg
                        headers = {
                            'X-Access-Token': os.getenv(ACCESS_TOKEN, ''),
                            'Content-Type': 'image/jpeg'
                        }

                        params = {
                                'token': ACCESS_TOKEN,
                            }
                    
                        json_data = {
                                'message': {
                                    'text': f'@{sender}',
                                    'sender_id': SENDER_ID
                            },
                        }
                        #response = requests.post(https://image.groupme.com/pictures?url=<https://eyestoseetherevelation.com/wp-content/uploads/2022/12/EDHH93-1280x640.jpg>, headers=headers, json=json_data, params=params)
                        continue

                else: #if NONE of the words are in the bible
                    # Respond to the test message
                    # curl_command = f"curl -d '{"text" : "Your message here", "bot_id" : "e20619c8b4652348f8511c2349"}' https://api.groupme.com/v3/bots/post"
                    
                    headers = {
                        # Already added when you pass json=
                        # 'Content-Type': 'application/json',
                    }

                    params = {
                        'token': ACCESS_TOKEN,
                    }

                    json_data = {
                        'message': {
                            'text': MESSAGE,
                            'sender_id': SENDER_ID,
                        },
                    }

                    response = requests.post(f'https://api.groupme.com/v3/groups/{GROUP_ID}/messages', params=params, headers=headers, json=json_data)

                        
                        # os.system(curl_command)
                #To add: Keeping track of the previous 10-20 messages, and sending some response if they are all above like 50% impure?
                #To add: Custom callouts for user_id's beyond mentioning (ex: seeing jess sent a message and )

        time.sleep(1)  # Poll every 1 seconds

if __name__ == "__main__":
    get_messages(None)
    #print_new_messages()

#curl -d '{"text" : "Your message here", "bot_id" : "e20619c8b4652348f8511c2349"}' https://api.groupme.com/v3/bots/post
# import requests

# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
# }

# data = '{"text" : "Your message here", "bot_id" : "e20619c8b4652348f8511c2349"}'

# response = requests.post('https://api.groupme.com/v3/bots/post', headers=headers, data=data)
