# Shadow-Watch
Security tool to monitor your resource usage and network for suspicious activity

#### Shadow-Watch

this program was made for educational purposes to monitor your network for suspiscious activity
and watch rescource usage on your device. you will need 'psutil'


MonitorStation: this is your terminal to run the program

This is a Python script that runs a set of other Python scripts in separate command prompt windows. Before running the scripts, the program prompts the user to enter a password. The program then checks the entered password against a stored password, and if the password is correct, it runs the set of scripts one by one.

The program first gets the current directory using the os.getcwd() function. It then defines the number of password attempts allowed as max_attempts = 3.

Next, the program defines a function get_credentials() that checks if a file named "credentials.txt" exists in the current directory. If the file exists, it reads the encoded credentials from the file, decodes them, and returns the username and password. If the file does not exist, it prompts the user to enter a username and password, encodes them, and saves them in the "credentials.txt" file. The function returns the username and password.

The program then calls the get_credentials() function to get the username and password. It defines a variable num_attempts to track the number of password attempts, and a function check_password() to prompt for the password and check if it's correct. The check_password() function compares the entered password against the stored password. If the entered password is correct, the function returns True. If the entered password is incorrect, the function increments num_attempts, and if num_attempts reaches max_attempts, the function prints an error message and starts the loadbar.py script using the subprocess.Popen() function. If the entered password is incorrect but num_attempts has not reached max_attempts, the function prints a message asking the user to try again, and returns False.

The program then enters a loop that repeatedly calls the check_password() function until the function returns True.

If the password is correct, the program defines a list scripts that contains the names of the scripts to run. The program then loops through the list of scripts, and for each script, it checks if the script file exists in the current directory. If the file exists, the program starts a new command prompt window using the subprocess.Popen() function and runs the script in the new window. If the file does not exist, the program prints an error message.

After running all the scripts, the program prints a message indicating that all the scripts have been started.

#### Sniffer:

This program continuously monitors system resource usage, such as CPU usage, memory usage, disk usage, temperature, power status, battery percentage, and time left until the battery is drained. It also includes a function to ping a specified host and return the latency (in milliseconds) of the ping.

The program uses the psutil library to gather system resource usage data and the subprocess library to run the ping command. The ping function uses the subprocess.run() method to run the ping command with the specified host and capture the output. It then parses the output to extract the latency value and returns it.

The main loop of the program continuously gathers the system resource usage data using psutil and formats it into a string to be printed to the console. The program uses the formatted cpu_usage_str variable in the print statement to handle the case where the CPU usage is unknown.

The program runs indefinitely until it is manually stopped.

#### Rescource-Graph:

This program is a system monitor that displays real-time information about the system's RAM usage, CPU usage, and network bandwidth usage in the terminal. The program uses the psutil module to gather system information and the os module to set the terminal size.

The load_bar function takes in a percentage and a width parameter and returns a string representation of a load bar with the specified width and percentage.

The main function sets the terminal size to a height of 7 and a width of 100.

The program then enters an infinite loop where it continuously gathers system information using the psutil module and displays the information in the terminal using load bars and percentages with labels. The program moves the cursor to the beginning of the previous line and clears it before printing the updated load bars to give the appearance of updating in place. The program waits for a short period (0.1 seconds) before updating again.

The program runs continuously until it is interrupted by the user.

#### Rescource-Monitor:

This is a Python program that monitors system information such as CPU usage, memory usage, disk usage, temperature, power status, and battery percentage. It uses the psutil library to retrieve system information and subprocess library to ping a specified host. The program runs an infinite loop that periodically prints the system information to the console. The CPU usage is retrieved using the psutil.cpu_percent() function with an interval of 3 seconds. The memory usage is retrieved using the psutil.virtual_memory() function. The disk usage is retrieved using the psutil.disk_usage() function. The temperature is retrieved using the psutil.sensors_temperatures() function. The power status and battery percentage are retrieved using the psutil.sensors_battery() function. If the ping to the specified host fails, the latency is set to None. Overall, this program provides useful system information for monitoring the health of a computer system.

#### Loadbar:

This program defines a progress bar function progress_bar() that simulates the encryption of personal files on a computer. The function prints a message "Encrypting personal files on your computer..." followed by a progress bar that fills up as the encryption progresses. The progress bar is represented by a string of 20 blocks, each block being a filled or empty character. The progress bar is updated every second to show the percentage of the encryption progress from 0% to 100%, in increments of 5%. After the encryption is completed, a message "Encryption complete. Have a nice day!" is printed.

#### Advisment:
This program was created for educationl purposes and for security reasons. DO NOT USE on any device you do not own or have pre documented aproval to use this on.
