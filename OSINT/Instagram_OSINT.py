import os
import sys
import json
import requests

# Function to get information about an Instagram user
def get_user_info(username):
    # Instagram API endpoint
    url = f"https://www.instagram.com/{username}/?__a=1"
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        user_info = {
            "username": data["graphql"]["user"]["username"],
            "full_name": data["graphql"]["user"]["full_name"],
            "profile_picture": data["graphql"]["user"]["profile_pic_url_hd"],
            "is_private": data["graphql"]["user"]["is_private"],
            "is_verified": data["graphql"]["user"]["is_verified"],
            "followers": data["graphql"]["user"]["edge_followed_by"]["count"],
            "following": data["graphql"]["user"]["edge_follow"]["count"],
            "posts": data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
        }
        print(json.dumps(user_info, indent=4))
    except:
        print("An error occurred.")

# Check if the script is being run in Kali Linux
if os.uname()[1] != "kali":
    print("This script is intended to be run in Kali Linux.")
    sys.exit()

# Get the Instagram username from the command line arguments
if len(sys.argv) < 2:
    print("Usage: python instagram_osint.py <username>")
    sys.exit()
username = sys.argv[1]

# Get information about the Instagram user
get_user_info(username)
