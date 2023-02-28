import os
import time

# Set the path to the Windows temp directory
temp_dir = os.environ['TEMP']

# Get the initial list of files in the temp directory
initial_files = os.listdir(temp_dir)

# Loop indefinitely to monitor for changes
while True:
    # Wait for 5 seconds before checking for changes again
    time.sleep(5)

    # Get the current list of files in the temp directory
    current_files = os.listdir(temp_dir)

    # Find the new files that were added since the last check
    new_files = [f for f in current_files if f not in initial_files]

    # Print the new files that were added
    if new_files:
        print("New files added to the temp directory:")
        for f in new_files:
            print("- {}".format(os.path.join(temp_dir, f)))

    # Find the files that were deleted since the last check
    deleted_files = [f for f in initial_files if f not in current_files]

    # Print the files that were deleted
    if deleted_files:
        print("Files deleted from the temp directory:")
        for f in deleted_files:
            print("- {}".format(os.path.join(temp_dir, f)))

    # Update the initial list of files with the current list
    initial_files = current_files
