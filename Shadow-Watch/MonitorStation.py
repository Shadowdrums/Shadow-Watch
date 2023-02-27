import subprocess
import os
import getpass
import base64

# Get the current directory
current_directory = os.getcwd()

# Define the number of password attempts allowed
max_attempts = 3

# Define a function to get the credentials
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

# Get the username and password
username, password = get_credentials()

# Define a variable to track the number of attempts
num_attempts = 0

# Define a function to prompt for the password and return True if it's correct
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

# Prompt for the password
while not check_password():
    pass

# Define a list of the scripts to run
scripts = ['Sniffer.py', 'Rescource-Monitor.py', 'Rescource-Graph.py']

# Run the scripts one by one in separate windows
if num_attempts != max_attempts:
    for script in scripts:
        script_path = os.path.join(current_directory, script)
        if os.path.exists(script_path):
            subprocess.Popen(f"start cmd /c python \"{os.path.join(current_directory, script)}\"", shell=True)
        else:
            print(f"Error: Could not find script {script_path}")

print("All scripts have been started.")
