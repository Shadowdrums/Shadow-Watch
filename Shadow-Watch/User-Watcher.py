import os
import getpass
import time
import base64

# Get current user name
username = getpass.getuser()

# Create log file
log_file = f"C:\\Users\\{username}\\Documents\\monitor.log"
with open(log_file, "a") as f:
    f.write("Monitoring started at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

# Create snapshot of data being monitored
snapshot_file = "UserData.txt"
if os.path.exists(snapshot_file):
    print(f"{snapshot_file} already exists. Monitoring will proceed without creating a new snapshot.")
else:
    with open(snapshot_file, "wb") as f:
        # Add monitored values to snapshot
        permissions = os.popen(f"net user {username}").read()
        processes = os.listdir("C:\\Windows\\System32")
        files = os.listdir(f"C:\\Users\\{username}")
        snapshot = f"User permissions:\n{permissions}\n\nProcesses:\n{processes}\n\nFiles:\n{files}"
        
        # Write snapshot to file and encode in base64
        f.write(base64.b64encode(snapshot.encode("utf-8")))
        print(f"Created new {snapshot_file} and added current snapshot of monitored data.")

# Initial state of monitored values
prev_permissions = None
prev_processes = set(os.listdir("C:\\Windows\\System32"))
prev_files = set(os.listdir(f"C:\\Users\\{username}"))

print("Monitoring started. Press Ctrl+C to exit.")

while True:
    try:
        # Check for changes in user permissions or privileges
        permissions = set(os.popen(f"net user {username}").read().split())
        if prev_permissions and prev_permissions != permissions:
            with open(log_file, "a") as f:
                f.write("User permissions changed at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                print("User permissions changed.")

        prev_permissions = permissions

        # Check for suspicious processes running in the background
        processes = set(os.listdir("C:\\Windows\\System32"))
        if prev_processes and prev_processes != processes:
            with open(log_file, "a") as f:
                f.write("New processes detected at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                print("New processes detected.")

        prev_processes = processes

        # Check for unexpected file modifications or deletions
        files = set(os.listdir(f"C:\\Users\\{username}"))
        if prev_files and prev_files != files:
            with open(log_file, "a") as f:
                f.write("File modifications or deletions detected at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                print("File modifications or deletions detected.")
        prev_files = files

        time.sleep(60)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        break
