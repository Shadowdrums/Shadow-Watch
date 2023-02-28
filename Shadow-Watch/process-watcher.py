import psutil
import time

# Get the list of current processes
current_processes = [(p.name(), p.pid) for p in psutil.process_iter()]

# Print the current list of processes
print("Current processes:")
for process, pid in current_processes:
    print(f"{process} (PID: {pid})")

# Loop indefinitely to monitor for changes
while True:
    # Wait for 5 seconds before checking for changes again
    time.sleep(5)

    # Get the updated list of processes
    updated_processes = [(p.name(), p.pid) for p in psutil.process_iter()]

    # Find the new processes that were started since the last check
    new_processes = [(p, pid) for p, pid in updated_processes if p not in [p for p, _ in current_processes]]

    # Print the new processes that were started
    if new_processes:
        print("\nNew processes started:")
        for process, pid in new_processes:
            print(f"{process} (PID: {pid})")

    # Find the processes that were stopped since the last check
    stopped_processes = [(p, pid) for p, pid in current_processes if p not in [p for p, _ in updated_processes]]

    # Print the processes that were stopped
    if stopped_processes:
        print("\nProcesses stopped:")
        for process, pid in stopped_processes:
            print(f"{process} (PID: {pid})")

    # Update the current list of processes with the updated list
    current_processes = updated_processes
