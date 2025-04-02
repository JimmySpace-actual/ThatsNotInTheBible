import requests
import time
import sys
import os
import random

# Replace these with your bot's info
ACCESS_TOKEN = sys.argv[1]
GROUP_ID = sys.argv[2]
SENDER_ID = sys.argv[3]

person_to_id = {'Theresa': '99094475', 'Evan Diercks': '93569276', 'Miller, Amber': '125871007', 'Benlin': '125871001', 'Olivia Roden': '73122709', 'anaya c': '125871061', 
'Luke Holecek': '115789922', 'Logan Sardina': '48502977', 'Ayo Dugbo': '62250664', 'Elena': '124994316', 'Noah Boyer-Edwards': '62444176', 'Diego Medina Carlin': '72864647', 
'Cesar M': '99336029', 'Lilly Dodge': '125154266', 'Mallika': '85864848', 'Jack Smolen': '125466007', 'Amer': '125871832', 'Jackson Childers': '93597007', 'Mahmoud Alramahi': '110075518', 
'Vihaan Shah': '125137741', 'Rodgers, Kate': '125846152', 'Shivam kaushik': '96022828', 'Tuna Tunçer': '125440094', 'Mohammed alramahi': '106611880', 'Annika B': '54740913',
 'Jimmy Xiao': '107138914', 'Damien Soubassis 7449069': '91301656', 'T 10': '61675457', 'Ari Frost': '117420080', 'Anusha Muralidhar': '12717363', 'Marco Gonzalez': '87998675', 
 'Vijay Daita': '117386227', 'Jolette': '119652560', 'Martina Cernakova': '124633847', 'Abhinav Garg': '106105866', 'Castells, Noah Salvador': '120404240', 'Tanvi Kurundkar': '125295284',
  'Blancas, Marco': '124658817', 'Raziel Rogers': '125516339', 'Mais': '118725514', 'Aditi Dixit': '95796861', 'Skylar': '59648199', 'Olivia Yu': '128031248', 'Lena Wu': '118629940',
   'Rich, Madilyn Grace': '125067179', 'Madison Jones': '88237458', 'Lynne Jung': '106054420', 'Azel Erck': '125871874', 'Varshitha': '116725866', 'Dumb': '47150673', 
   'Mary Donlon': '34604117', 'sharon™️': '27584880', 'Posterior Images': '12509355', 'lil houseplant🌿': '35861874', 'Thiccy Dumb': '26665484', 'Oscar Laínez': '41303436', 
   'Jolene/Doppler': '74501675', '\'Jonny Smith': '36090275', 'Sage Larson': '40870457', 'Jakob Spagna Eldridge (Krieg)': '32200343', '✧･ﾟ: *✧･ﾟ♡*(ᵘwᵘ)*♡･ﾟ✧*:･ﾟ✧ (◕‿◕✿)': '50069551', 
   "Daniel O'Brien": '12714517', 'Stephen Elliott': '29806899', 'Celie Sanchez': '67519730', 'Jonathan W': '43046093', 'Kawai Cheung': '25616256', 'Canucklehead': '32087449', 
   'Sanjna M.': '52136971', 'Alejandro Alvizuri': '22715197', 'Angela Jaw': '28166728', 'Sam Shirley': '28198221', 'Cordarro': '75673190', 'Hayden': '42845962', 'Nicole': '43113943', 
   'Matt Lyons': '14295017', 'Haley Prochilo': '18967496', 'Katherine East': '29046668', 'Megan Geyer': '27948857', 'Esh': '74585993', 'Andrew Porter': '38664371', 
   'Nick Qualizza': '46036292', 'Jack Gronenthal': '20468350', 'Chris Ertman': '38187272', 'Ling-Ling Menez': '32661932', 'Jessica Wolford': '20540053', 'Evelyn Krasnik': '7794501', 
   'Carmen Gutiérrez': '52609830', 'Jane Chun': '19211832', 'Alison Brandvold': '53549111', 'Look At The Thicc Of Dat Wrist': '73238166', 'Derp': '59507911', 'Martin Chlopecki': '44286298',
    'Stupid Bitch': '53646000', 'Jacob Maxia': '26476463', 'Sri Subramanian': '20774747', 'Sofia Jauregui': '34430052', 'William Drennan': '29051041', 
    'Jake Basile Frederick': '74422671', 'Olivia Runne': '63226491', 'Eric Jiang': '61660160', 'Oh yeah that one guy who’s not there often anymore': '41715155', 
    'Manav Modi': '74321796', 'Riley': '19212976', 'Valerie Shamshyna': '76253077', 'phat ass': '33059217', 'Matt T': '41735417', 'bitch (retired and old)': '74414027', 
    'Halfwit': '19985417', 'Justin Kust': '74851802', 'Alex Osepek': '70980137', 'Nimisha Gupta': '59218970', 'Paul Malachuk': '26388391', 'Conor Devlin': '50208903', 
    'Davis Zhu': '86062641', 'Tyler Fals': '87045567', 'Kishan Patel': '12588763', 'Amanda Hoika': '46852950', 'Amber Moore': '82147726', 'Pranav Goel': '65761563', 
    'Jake Mitstifer': '50526131', 'Natasha Sherlock': '71700882', 'Lorraine': '86529721', 'Mercedes Benz': '74502770', 'Claire von Ebers': '46197472', 'Marisol Perez Zuniga': '87328369', 
    'Kyle 2': '60019859', 'Elisa Segura': '39688582', 'Rajee S': '59184906', 'Jeffrey Y': '44634703', 'Leah': '88433520', 'Costello sleep 💤': '86008937', 
    'Crystal Mandal [She/They]': '45510684', 'Aakash': '87141419', 'alex is gone': '38780679', 'Yang Xiao': '89097259', 'Tej Inuganti': '88339681', 'Jakob Freeman': '87076947', 
    'Yumeng Zhang （Daisy）': '75346392', 'Ajay Raigaga': '69296040', 'Jidapa Thia': '35745701', 'Izzy L': '56228904', 'Tejesh Bhaumik': '91291737', 'Anudeep Ekkurthi': '63280524', 
    'Linnie Shapiro': '40563504', 'Sohail Khan': '30991493', 'Sharvil Garg': '87420923', 'Çêrø': '80414071', 'Tejesh Bhaumik 2': '85075392', 'Mark Jamil': '74472493',
     'Yang Xiao 2': '31697753', 'Im.not.old.': '32638183', 'Zayaan Ali': '90884649', 'Peter Giannetos': '51264762', 'avatar shinu the great wizard of the nfl': '87226249', 
     'Charter (Peter Gutknecht)': '48981659', 'Olo': '37281741', 'Leah Uteg': '69926563', 'Logan M': '56035406', 'aku': '92013354', 'Michael Greco': '54871784', 
     'Aseem Patra': '95750800', 'Ajosh Antony': '87433535', 'James': '25940444', 'Tama (Morgan)': '66433379', 'Ashton Su (they/them)': '95737122', 'Brian': '16657129', 
     'Jon Mastrud': '49830341', 'Kalina Simeonova': '96063638', 'Piss Baby': '63315152', 'Seema Chakra': '88102349', 'Maddie Blaauw': '46182836', 'FishBish': '96127480', 
     'Amir': '74210293', 'Jeffery Kao': '87332181', 'Zayd Khan 4': '75256717', 'Zane Schneider': '96731511', 'Advaith Bala': '92449614', 'AJ': '75778074', 'Celia': '58249569', 
     'Katelyn': '62410853', 'The Lord': '33430670', 'Tianna Blake': '68251604', 'Celia Thome': '96579963', 'hysues': '91019808', 'Talia Petty': '71734641', 
     'Cunt (Gone With The Wind)': '95860733', 'Alex Ishmael': '95830257', 'James Meadows': '95798788', 'Fiza Goyal': '37639383', 'Kilometerzzzz': '41590063', '(Shr)avatar Kat': '52523269', 
     'Julia 🐞': '58692538', 'Diego Orellana': '82015769', '🐕 🐩 🐶': '43709601', 'Aashish Subramanian': '95575081', 'Jovan Taylor': '87469008', 'Kenneth Chuang': '50231915', 
     'Veena Saraswathula': '20035948', 'Amy G': '85497618', 'Rashmi Ghonasgi': '63765013', 'Ethan Mattson': '60748571', 'Riya Gupta': '35165265', 'Shawn Arreguin': '18473102', 
     'Anna Przybyl': '31997785', 'Lucas Seibold': '74444902', 'Carson Van Wassenhove': '29377308', 'Sam L': '79647539', 'Hamza': '97178539', 'tyler the ball creator': '38614349', 
     'Jasmine Ng': '49857461', 'Vector (Akash)': '93465366', 'PJ Beigh': '36060511', 'Hawk Chang': '95730233', 'Brendan Mohen': '74688198', 'Ben Xie': '36741722', 
     'Tommy Hummel': '86268062', 'Andrew Lum': '95522915', 'Sanjana Kirugulige': '22540301', 'paula m': '55606765', 'Mrs. Rooster': '55257260', 'Rowan Abzug': '59520522', 
     'will': '56701101', 'Abhiram': '94402197', 'Double Trouble': '19979359', 'laurne': '91457484', 'Isrealp': '74182611', 'ishika, perchance': '46707233', 'Matthew R.': '87158934', 
     'Mello, Charles': '99994687', 'Gabi Miller': '97851553', 'Tony Anastasia': '103274202', 'Nicole P': '103123599', 'Giridhar, Varun': '96107837', 'Rhanda Halawah': '68522091', 
     'Mickie Odom': '41250211', 'Will Curtis': '51703786', 'Josh Greenberg': '104982120', 'Willis Le': '63180669', 'Qiran Pang': '99853820', 'Rachel Hoffman': '86086864', 
     'Archie': '37518015', 'Anshul Bheemreddy': '90860845', 'Krishna Nimmalagadda': '54166517', 'Dominika': '79111390', 'Meredith Johnson': '74758280', 'April Wendling': '37389434', 
     'Rachel Sun': '50973854', 'Caroline Atkinson': '44312501', 'Kristin': '95692272', 'Denver Merz': '81199409', 'Sonali Merchia': '85574515', 'Gabriel Dizon': '83367937', 
     'Joshua A': '110650601', 'Zubair Lalani': '28339823', 'Joey Shepin': '57190586', 'Ethan Cho': '74095077', 'Token Connecticuter': '110650861', 'laurne’s (ex) gf': '60196582', 
     'Maddy Meyer': '74414949', 'Adrian Pawlikowski': '105894419', 'liz <3': '87410204', 'Colin OB': '105102772', 'Alex Meindl': '50333136', 'Jett Miller': '52379907', 
     'Max Goldstein': '86573155', 'Alex Eilert': '107815140', 'Olivia Furlano': '95572087', 'MJ Al-Khabouri': '87702221', 'Dylan Scott': '82212067', 'Liam Thompson': '110640373', 
     'Shaurya Gupta': '95854130', 'Vid  Gautam': '95581734', 'Mosie Jartin': '72901167', 'miss margs': '57742146', 'Jacobble': '110649582', 'Kendra Riddle': '58014482', 
     'Ryan McAllister': '95690548', 'Welby': '31621064', 'Brandon White': '54080500', 'Sam Pfister': '69181775', 'John Connolly': '35181625', 'Claire Baffes': '37217876', 
     '田欣怡 麻': '116075826', 'amy c.': '67825450', 'Alisha Kulkarni': '103493137', 'Pramod Prem': '45160494', 'Emaly Culich': '100204367', 'James S': '95859529', 
     'Michael Escobedo': '95562631', 'Sorin Pollock': '34966381', 'Aidan Stahl': '105167536', 'Emma Barrera': '116091880', 'Meenakshi De': '116207801', 'Finn Buda': '98063143', 
     'Alejandro H.': '113164466', 'Krishna': '48917316', 'DiCarlo': '88112039', 'Rowan Mertz': '84291047', 'Jack Fleishman': '73236271', 'Zach Ramos': '87101993', 
     'Zoe Ahluwalia': '99089569', 'Nathan Lin': '42195534', 'Kallee Smaha': '79659970', 'Neighcion 🐴🌎 (Emma S)': '116082807', 'Sofia Pajak': '105186364', 'Moris J': '115793798', 
     'Nathalie Andrade': '72545783', 'Clemens Walter': '116065604', 'Felipe Boaventura': '50352607', 'Reece Jacobson': '49426788', 'Makaila Mburu': '98588253', 'Nicole 2': '116692047', 
     'elizabeth': '65702370', 'Celine Espino': '99423237', 'Anna Shurdhi': '74536386', 'Amaan Mirza': '42029228', 'Vonne Eichten': '116692317', 'Evan McPheron': '116692293', 
     'Michaela': '116065336', 'Low Taper Tommy': '58858467', 'Joseph Caya': '73190278', 'Emma Joyce': '105846309', 'Ric': '116115546', 'Milly Manno': '24100573', 
     'Ryan Ilgen': '73099707', 'Christiana Lewis': '95554547', 'Natalie Tran': '55447044', 'Megan Meade': '49614887', 'Anirudh Moholkar': '80538253', 'Kay Rivera': '116692181',
      'Isabella Grows': '116481382', 'Violet Merz': '98393289', "Aidan O'Dell": '89825835', 'Sean De Castro': '97522879', 'Alex 🪬': '79407900', 'Lea': '117283032', 
      'Kayleigh White': '116847166', 'Noah Meyerhoff': '66902627', 'Hans Manganti': '110487819', 'Eryn Van Wijk': '111125888', 'Nikhil Sivakumar': '550201930', 
      'Kelsey Green': '73543265', 'Hartej Sandhu': '78005235', 'Saipranav Venkatakrishnan': '120150397', 'Jeff': '120152300', 'Addy': '41522840', 'leonard hall': '99690044', 
      'Andrew Robinson': '73813238', 'Joey': '116931043', 'Kerker, Michael Nicholas': '72791776', 'Daden': '94381553', 'Ibrahem Ellaicy': '116275457', 'Ina Pudipeddi': '120153052',
       'D Whore (Dalton L)': '120151215', 'Parker Johnson': '95790312', 'Caden Eichenlaub': '115842673'}

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
                    continue

                else:
                    send_message("NONE of these words are in The Bible, you are going straight to Hell", sender_name, sender_id)
                
                

        time.sleep(1)

if __name__ == "__main__":
    print_new_messages()