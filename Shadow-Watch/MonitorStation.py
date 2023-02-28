import subprocess
import os
import getpass
import base64

current_directory = os.getcwd()

max_attempts = 3

def get_credentials():
    credentials_file = "credentials.txt"
    if os.path.isfile(credentials_file):
        with open(credentials_file, "rb") as f:
            encoded_credentials = f.read()
        credentials = base64.b64decode(encoded_credentials).decode().split(":")
        username = credentials[0]
        password = credentials[1]
        return username, password
    else:
        print("No credentials file found.")
        print("Creating new credentials.")
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        encoded_credentials = base64.b64encode(f"{username}:{password}".encode())
        with open(credentials_file, "wb") as f:
            f.write(encoded_credentials)
        return username, password

username, password = get_credentials()

num_attempts = 0

def check_password():
    global num_attempts
    pw = getpass.getpass("Enter the password to start the scripts: ")
    if pw == password:
        return True
    else:
        num_attempts += 1
        if num_attempts == max_attempts:
            print("Incorrect password entered too many times. Running the loadbar script...")
            subprocess.Popen(f"start cmd /c python \"{os.path.join(current_directory, 'loadbar.py')}\"", shell=True)
            return True
        else:
            print("Incorrect password. Please try again.")
            return False

while not check_password():
    pass

scripts = ['Sniffer.py', 'Rescource-Monitor.py', 'process-watcher.py', 'temp-watcher.py', 'User-Watcher.py']

if num_attempts != max_attempts:
    while True:
        print("Select a script to run:")
        for i, script in enumerate(scripts):
            print(f"{i+1}. {script}")
        choice = input("Enter the number of the script to run (or 'q' to quit): ")
        if choice == 'q':
            break
        elif choice.isdigit() and int(choice) in range(1, len(scripts)+1):
            script_path = os.path.join(current_directory, scripts[int(choice)-1])
            if os.path.exists(script_path):
                subprocess.Popen(f"start cmd /c python \"{script_path}\"", shell=True)
                input("Press Enter to continue...")
                os.system('cls' if os.name=='nt' else 'clear')
            else:
                print(f"Error: Could not find script {script_path}")
        else:
            print("Invalid choice. Please try again.")

print("All scripts have been started.")
