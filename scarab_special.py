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

                text = message.get("text") or ""
                attachments = message.get("attachments", [])
                sender_name = message.get("name", "Unknown")
                sender_id = message.get("sender_id")

                print(f"New message: {text} from {sender_name}")
                message_words = text.lower().split()

                # Skip short messages
                if len(message_words) < 3:
                    continue

                message_set = set(message_words)

                # if text == "" and attachments:
                #     send_message("you think I can't see your impure images? Lord sees all, impure images, impure thoughts, impure.... believe me I wish I couldn't", sender_name, sender_id)
                #     continue

                if message_set & bible_words:
                    impurity = 100 * ((len(message_set) - len(message_set & bible_words)) / len(message_set))

                    if impurity == 0:
                        send_message("You are a pure soul, a holy spirit, a bright beacon of light in this hellish abyss, the only Saint to be found in this land of Sinners. The Gates of Heaven are open to you and you alone, welcome to My Kingdom child.", sender_name, sender_id)
                    else:
                        # send_message(f"Your thoughts are {impurity:.1f}% impure", sender_name, sender_id)
                        m = ""
                        if sender_id == '65702370':
                            m = "Stop with these impure words. You are Elizabetter than that."
                        elif sender_id == '116692293':
                            m = "I know you will EVANtually stop speaking these imppurities, but I want you to STOP NOW."
                        elif sender_id == '125137741':
                            m = "Vi-haandle these jokes with anger and a trip to hell."
                        elif sender_id == '93597007':
                            m = "jackSON you are a sinner in saying these impurities."
                        elif sender_id == '110075518':
                            m = "You should not have the mahMOOD to say all of this."
                        elif sender_id == '125846152':
                            m = "These impure words should vaKATE your mouth."
                        elif sender_id == '125871832':
                            m = "Amer-ica is a land of sinners, and you are one of them."
                        elif sender_id == '96022828':
                            m = "shivam? more like shivampire with the kind of language you are using."
                        elif sender_id == '116186638':
                            m = "I don't even try to help ghosts, you are already gone."
                        elif sender_id == '105500444':
                            m = "You could be a-deity, but you are not."
                        elif sender_id == '125449111':
                            m = "I can\'t belive you are an-AKIN to such language."
                        elif sender_id == '106105866':
                            m = "You should abhi-never say these words again."
                        elif sender_id == '106054420':
                            m = "Words like these will make you violynnet"
                        elif sender_id == '87702221':
                            m = "You could say you are mJK, but you should not be speaking this even as a joke."
                        elif sender_id == '129268766':
                            m = "You AREiana not excused."
                        elif sender_id == '59648199':
                            m = "If you speak better language, you will go to the SKYlar, the heaven."
                        elif sender_id == '69263937':
                            m = "You are a dillonquint in saying all of this."
                        elif sender_id == '58692538':
                            m = "Ju-liar, you sinner, you must speak better language."
                        elif sender_id == '95750800':
                            m = "A-SEEMingly innocent person, disguising his sinful language under his CAPtaincy. You need to set a better example."
                        elif sender_id == '87076947':
                            m = "JaKOPING with foul language will not help."
                        elif sender_id == '120150397':
                            m = "The Lord will SAIde with you, if you choose to not use these impure words."
                        elif sender_id == '95859529':
                            m = "You are a silly-one, sullivan, but jokes will not led your impurity slide."
                        elif sender_id == '50352607':
                            m = "You will feli-pay for your sins."
                        elif sender_id == '57742146':
                            m = "Your MaJESSty, I did notice you, and scanned your foul language. Now stop JESSting around and start setting a better example for your juniors."
                        elif sender_id == '73190278':
                            m = "It is not all a JOke, you need to learn to either speak purer words or keep your mouth shut."
                        elif sender_id == '48917316':
                            m = "I could krishNAME you the winner of the sinner award, with the kind of language you use."
                        elif sender_id == '73543265':
                            m = 'You will kelSEY it for yourself, your punishments in hell, with this kind of language.'
                        elif sender_id == '69181775':
                            m = "You speak foul language, I do not, we are not the SAMe"
                        elif sender_id == '116692047':
                            m = "I will niCALL you out for your sins, and you will be punished, if you keep up with this kind of language."
                        elif sender_id == '50201930':
                            m = "You would make a niKHILler saint, if only you don't commit so many sins of language."
                        elif sender_id == '95562631':
                            m = "There was saint Michael, and then there is you. I guess this long life was bound to give me disappointments."
                        elif sender_id == '116091880':
                            m = "Emma leave you to your own foul language, I have started losing all hope."
                        elif sender_id == '105167536':
                            m = 'If you need aid-in imporoving your language, I will willingly do that.'
                        elif sender_id == '103493137':
                            m = "Your mouth needs a-leash-a means of controlling this foul language."
                        elif sender_id == '105186364':
                            m = 'There are so-few words not in the bible, and yet you use them. I guess this long life was bound to give me disappointments.'
                        elif sender_id == '100204367':
                            m = "Imma-leave you to your own foul language."
                        else:
                            m = f"Your thoughts are {impurity:.1f}% impure"

                        send_message(m, sender_name, sender_id)


                elif not text.strip() and attachments:
                    send_message("you think I can't see your impure images? Lord sees all, impure images, impure thoughts, impure.... believe me I wish I couldn't", sender_name, sender_id)
                    # image_urls = [
                    #     "https://en.wikipedia.org/wiki/File:Buddy_christ.jpg",
                    #     "https://curious-archive.b-cdn.net/wp-content/uploads/danilo-wolf-angel-23-1024x644.jpg",
                    #     "https://static1.squarespace.com/static/610e8a1442e2e073cafbc00f/6110f5866397ce460361d3dd/63f5e0e59c152d5aa7dca368/1677480227546/1505490457119557293.jpg?format=1500w",
                    #     "https://i.pinimg.com/474x/38/9d/5f/389d5f3ac9f92038c261602c13d82d88.jpg",
                    #     "https://gregatkinson.com/wp-content/uploads/2013/06/loser-600x450.jpg",
                    #     "https://eyestoseetherevelation.com/wp-content/uploads/2022/12/EDHH93-1280x640.jpg",
                    #     "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZhOBCe0Sc0hkm36i0QqyznzJ7LwjTTKEawujCQDcIZQzg2nred260UMzrjp1Dt7gQCMMlO3bNZ_LJVoCxHPruET0Z4DvnEN3acA8ZcStSlxreLsVZFc0LIUkdbEyZTNTCsfkZdJuY-rY/s400/Jesus-Christ-Limpias-Spain.jpg"
                    # ]
                    # image_url = random.choice(image_urls)
                    # send_message(f"[image] {image_url}", sender_name, sender_id)
                    continue

                else:
                    send_message("NONE of these words are in The Bible, you are going straight to Hell", sender_name, sender_id)
                
        time.sleep(1)

if __name__ == "__main__":
    print_new_messages()