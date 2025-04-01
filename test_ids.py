import requests
import sys

# Access token and group ID from command line arguments
ACCESS_TOKEN = sys.argv[1]
GROUP_ID = sys.argv[2]

def get_members():
    """Fetch the members of the GroupMe group."""
    url = f"https://api.groupme.com/v3/groups/{GROUP_ID}"
    params = {"token": ACCESS_TOKEN}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        members = response.json()["response"]["members"]
        member_dict = {member["nickname"]: member["user_id"] for member in members}
        return member_dict
    else:
        print(f"Error fetching members: {response.status_code} - {response.text}")
        return {}

if __name__ == "__main__":
    members = get_members()
    print("Member dictionary:")
    print(members)