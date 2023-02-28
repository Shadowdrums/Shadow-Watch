import psutil
import subprocess
import time
import datetime

def ping(host):
    """
    Returns the latency (in milliseconds) of a ping to the specified host.
    Returns None if the ping fails.
    """
    ping_output = subprocess.run(['ping', '-c', '1', '-W', '1', host], capture_output=True, text=True)
    if ping_output.returncode == 0:
        # Parse the ping output to extract the time
        time_index = ping_output.stdout.find('time=')
        if time_index != -1:
            time_str = ping_output.stdout[time_index + 5:]
            time_ms = float(time_str.split()[0])
            return time_ms
    return None

def generate_load_bar(percent, length):
    """
    Generates a load bar string with a solid fill based on the given percentage and length.
    """
    fill_length = int(percent / 100 * length)
    return f"[{'=' * fill_length}{' ' * (length - fill_length)}]"

while True:
    cpu_percent = psutil.cpu_percent(interval=3)

    # Check if cpu_percent is None before formatting it as a string
    if cpu_percent is not None:
        cpu_usage_str = f"CPU Usage: {cpu_percent}% {generate_load_bar(cpu_percent, 20)} |\n"
    else:
        cpu_usage_str = "CPU Usage: Unknown |\n"

    virtual_mem = psutil.virtual_memory()
    mem_percent = virtual_mem.percent
    mem_used = virtual_mem.used / (1024 * 1024)
    mem_total = virtual_mem.total / (1024 * 1024)

    partitions = psutil.disk_partitions(all=True)
    hdd_percent = 0
    ssd_percent = 0
    for partition in partitions:
        if 'cdrom' in partition.opts or partition.fstype == '':
            continue
        partition_usage = psutil.disk_usage(partition.mountpoint)
        if 'HDD' in partition.opts:
            hdd_percent += partition_usage.percent
        elif 'SSD' in partition.opts:
            ssd_percent += partition_usage.percent

    if hasattr(psutil, 'sensors_temperatures'):
        temps = psutil.sensors_temperatures(fahrenheit=True)
        if 'coretemp' in temps:
            temp = temps['coretemp'][0].current
        elif 'acpitz' in temps:
            temp = temps['acpitz'][0].current
        else:
            temp = 'Unknown'
    else:
        temp = 'Unknown'

    power_usage = psutil.sensors_battery()
    if power_usage is not None:
        if power_usage.power_plugged:
            power_status = "Plugged In"
        else:
            power_status = "Not Plugged In"
        power_percent = power_usage.percent
        power_time = power_usage.secsleft
    else:
        power_status = "Unknown"
        power_percent = "Unknown"
        power_time = "Unknown"

    print(f"{cpu_usage_str}"
      f"Memory Usage: {mem_percent}% {generate_load_bar(mem_percent, 20)} ({mem_used:.2f} MB / {mem_total:.2f} MB)\n"
      f"HDD Usage: {hdd_percent}% {generate_load_bar(hdd_percent, 20)}\n"
      f"SSD Usage: {ssd_percent}% {generate_load_bar(ssd_percent, 20)}\n"
      f"CPU Temperature: {temp} °F\n"
      f"Power Status: {power_status}\n"
      f"Battery Percentage: {power_percent}% {generate_load_bar(power_percent, 20)}\n"
      f"Time Left: {power_time} seconds\n")
time.sleep(0.1)  # wait for 0.1 seconds before printing the next set of stats.



