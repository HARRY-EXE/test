import os

directory_path = '/sdcard/HARRYv6/'

if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
    print(f"The directory '{directory_path}' does not exist or is not a valid directory.")
else:
    files = os.listdir(directory_path)

    if not files:
        print(f"No files found in the directory '{directory_path}'.")
    else:
        print("List of files:")
        for i, file_name in enumerate(files, start=1):
            print(f"{i}. {file_name}")

        while True:
            try:
                choice = int(input("Enter the number corresponding to the file you want to select: "))
                if 1 <= choice <= len(files):
                    selected_file = files[choice - 1]
                    print(f"You selected: {choice}. {selected_file}")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
