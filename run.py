def harryresults():
    ok_file_path = 'HARRYv6-OK.txt'
    cp_file_path = 'HARRYv6-CP.txt'

    if not (os.path.exists(ok_file_path) and os.path.exists(cp_file_path)):
        print("Files not found. Exiting.")
        return

    print("1 - CHECK OK FILES\n2 - CHECK CP FILES")
    user_choice = input("Enter your choice (1 or 2): ")

    if user_choice == '1':
        show_cookies = input("Show cookies? (y/n): ").lower() == 'y'
        process_file(ok_file_path, show_cookies)
    elif user_choice == '2':
        process_file(cp_file_path, show_cookies=False)
    else:
        print("Invalid choice. Exiting.")

def process_file(file_path, show_cookies):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        parts = line.strip().split('|')
        if show_cookies:
            print(f"{i} - {parts[0]} | {parts[1]} | {parts[2]}")
        else:
            print(f"{i} - {parts[0]} | {parts[1]}")

# Example usage
harryresults()
