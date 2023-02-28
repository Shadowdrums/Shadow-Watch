# Shadow-Watch
Security tool to monitor your resource usage and network for suspicious activity

#### Shadow-Watch

this program was made for educational purposes to monitor your network for suspiscious activity
and watch rescource usage on your device. you will need 'psutil' and 'scapy'

#### Summary:

This program is a Python script that allows the user to run multiple monitoring scripts on their computer. The scripts included are "Sniffer.py", "Resource-Monitor.py", "process-watcher.py", and "temp-watcher.py".

The program first prompts the user for a password to ensure that unauthorized users cannot run the monitoring scripts. The user has three attempts to enter the correct password before the program stops prompting and instead runs a separate script called "loadbar.py".

Once the user has entered the correct password, the program starts a loop that displays a menu of options to the user. The user can select which script they want to run by typing the number associated with the script. Once the user selects a script, the program uses the subprocess module to run the selected script in a new window.

After the desired script has been run, the program clears the terminal screen to prevent excessive terminal spam. The program then displays the menu of options again, allowing the user to select another script to run if they wish.


#### MonitorStation: this is your terminal to run the program

This program is a Python script that allows the user to run multiple monitoring scripts on their computer. The scripts included are "Sniffer.py", "Resource-Monitor.py", "process-watcher.py", and "temp-watcher.py".

The program first prompts the user for a password to ensure that unauthorized users cannot run the monitoring scripts. The user has three attempts to enter the correct password before the program stops prompting and instead runs a separate script called "loadbar.py".

Once the user has entered the correct password, the program starts a loop that displays a menu of options to the user. The user can select which script they want to run by typing the number associated with the script. Once the user selects a script, the program uses the subprocess module to run the selected script in a new window.

After the desired script has been run, the program clears the terminal screen to prevent excessive terminal spam. The program then displays the menu of options again, allowing the user to select another script to run if they wish.

#### Sniffer:

This program continuously monitors system resource usage, such as CPU usage, memory usage, disk usage, temperature, power status, battery percentage, and time left until the battery is drained. It also includes a function to ping a specified host and return the latency (in milliseconds) of the ping.

The program uses the psutil library to gather system resource usage data and the subprocess library to run the ping command. The ping function uses the subprocess.run() method to run the ping command with the specified host and capture the output. It then parses the output to extract the latency value and returns it.

The main loop of the program continuously gathers the system resource usage data using psutil and formats it into a string to be printed to the console. The program uses the formatted cpu_usage_str variable in the print statement to handle the case where the CPU usage is unknown.

The program runs indefinitely until it is manually stopped.

#### Rescource-Monitor:

This is a Python program that monitors system information such as CPU usage, memory usage, disk usage, temperature, power status, and battery percentage. It uses the psutil library to retrieve system information and subprocess library to ping a specified host. The program runs an infinite loop that periodically prints the system information to the console. The CPU usage is retrieved using the psutil.cpu_percent() function with an interval of 3 seconds. The memory usage is retrieved using the psutil.virtual_memory() function. The disk usage is retrieved using the psutil.disk_usage() function. The temperature is retrieved using the psutil.sensors_temperatures() function. The power status and battery percentage are retrieved using the psutil.sensors_battery() function. If the ping to the specified host fails, the latency is set to None. Overall, this program provides useful system information for monitoring the health of a computer system.

#### Loadbar:

This program defines a progress bar function progress_bar() that simulates the encryption of personal files on a computer. The function prints a message "Encrypting personal files on your computer..." followed by a progress bar that fills up as the encryption progresses. The progress bar is represented by a string of 20 blocks, each block being a filled or empty character. The progress bar is updated every second to show the percentage of the encryption progress from 0% to 100%, in increments of 5%. After the encryption is completed, a message "Encryption complete. Have a nice day!" is printed.

#### process-watcher:

This program is designed to monitor the running processes on a system and detect any changes in the processes. It starts by using the psutil library to get the list of current processes and prints them out. It then enters an infinite loop and sleeps for 5 seconds before checking for any changes in the process list.

If any new processes have started since the last check, it prints out their names and PIDs. If any processes have stopped, it also prints out their names and PIDs. Finally, it updates the current process list with the updated list so that it can compare against it during the next iteration of the loop.

This program can be useful for monitoring processes on a system and detecting any unexpected or unauthorized activity. It could be run as a background process to continuously monitor the system for changes.

#### temp-watcher:

This program monitors the Windows temp directory for any changes and prints out any new files that were added or files that were deleted since the last check.

The program starts by setting the temp_dir variable to the path of the Windows temp directory obtained through the os.environ function. The program then gets the initial list of files in the temp directory using the os.listdir function.

Next, the program enters an infinite loop that repeatedly waits for 5 seconds and then gets the current list of files in the temp directory using the os.listdir function. It then finds any new files that were added since the last check by comparing the current list of files to the initial list using list comprehension. Similarly, it finds any files that were deleted since the last check by comparing the initial list to the current list using list comprehension.

Finally, the program prints out any new files that were added or files that were deleted since the last check. It also updates the initial list of files with the current list so that it can correctly identify any new changes during the next iteration of the loop.

#### Advisment:
This program was created for educationl purposes and for security reasons. DO NOT USE on any device you do not own or have pre documented aproval to use this on.
