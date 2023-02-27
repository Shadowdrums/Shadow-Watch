import time

# Define the progress bar function
def progress_bar():
    print("Encrypting personal files on your computer...")
    print("[{}] 0%".format("█" * 20), end="\r")
    for i in range(21):
        print("[{}{}] {}%".format("█" * i, " " * (20 - i), i * 5), end="\r")
        time.sleep(1.0)
    print("[{}] 100%".format("█" * 20))
    print("Encryption complete. Have a nice day!")
    # Add your malicious code here

# Call the progress bar function
progress_bar()
