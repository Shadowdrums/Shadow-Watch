import os
import psutil
import time

# Define the load bar function
def load_bar(percent, width):
    bar_width = width - 10  # Leave 10 spaces for the percentage label
    load_width = int(bar_width * percent / 100)
    return '[' + '█' * load_width + '>' + ' ' * (bar_width - load_width) + f'] {percent}%'

def main():
    # Set the terminal size to a height of 15 and a width of 80
    os.environ['LINES'] = '7'
    os.environ['COLUMNS'] = '100'

while True:
    # Get the current RAM usage
    mem = psutil.virtual_memory()
    used = mem.used / (1024 * 1024)
    total = mem.total / (1024 * 1024)
    percent = mem.percent

    # Get the current CPU usage
    cpu_percent = psutil.cpu_percent()

    # Get the current network bandwidth usage
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent / (1024 * 1024)
    bytes_recv = net_io_counters.bytes_recv / (1024 * 1024)

    # Calculate the width of the terminal window
    width = 100

    # Draw the load bars and percentages with labels
    ram_bar = load_bar(percent, width)
    cpu_bar = load_bar(cpu_percent, width)
    net_send_bar = load_bar(bytes_sent, 50) # Set width to 50 for shorter bar
    net_recv_bar = load_bar(bytes_recv, 50) # Set width to 50 for shorter bar

    # Move the cursor to the beginning of the previous line and clear it
    print('\r\033[K', end='', flush=True)

    # Print the load bars and percentages with labels
    print(f"RAM: {ram_bar}\nCPU: {cpu_bar}\nNet Sent: {net_send_bar}\nNet Recv: {net_recv_bar}\n", end='', flush=True)

    # Wait for a short period before updating again
    time.sleep(0.1)

if __name__ == '__main__':
    main()
