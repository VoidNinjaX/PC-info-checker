import platform
import socket
import time
import sys
import os
import psutil
import shutil
import itertools 
from datetime import datetime

def progress_bar(message, duration):
    total_length = 30
    sys.stdout.write(f"{message} ")
    sys.stdout.flush()

    for i in range(total_length):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(duration / total_length)

    print(" Done!")

def live_clock():
    print("\nLive system time: Press Ctrl+C to stop\n")
    try:
        while True:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sys.stdout.write(f"\r{now}")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nClock stopped.")

def loading_animation(message, duration):
    print(message, end="")
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(next(spinner))  
        sys.stdout.flush()               
        time.sleep(0.1)                 
        sys.stdout.write('\b')          
    print(" Done!")

def collect_pc_info():
    loading_animation("Collecting PC information...", 3)

    system_info = {
        'PC Name': socket.gethostname(),
        'Operating System': platform.system(),
        'OS Version': platform.version(),
        'Machine Architecture': platform.machine(),
        'Processor': platform.processor(),
        'Node Name': platform.node(),
        'Platform': platform.platform(),
        'Release': platform.release(),
        'System': platform.system(),
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'Available Memory (GB)': round(psutil.virtual_memory().available / (1024 ** 3), 2),
        'Total Disk Space (GB)': round(shutil.disk_usage("/").total / (1024 ** 3), 2),
        'Used Disk Space (GB)': round(shutil.disk_usage("/").used / (1024 ** 3), 2),
        'Free Disk Space (GB)': round(shutil.disk_usage("/").free / (1024 ** 3), 2)
    }

    return system_info

def save_info_to_file(info, filename="PC_info.txt"):
    progress_bar("Saving information to file...", 2)

    with open(filename, 'w') as f:
        f.write("=== Advanced PC Information ===\n")
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

    print(f"PC information has been saved to {filename}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_github_message():
    print("\nThank you for using the PC Info Collector!")
    print("Please visit our GitHub for more exciting projects:")
    print("GitHub: https://github.com/ZuluStudiosInc")
    print("\nFeel free to explore and contribute!")

def main():
    clear_screen()

    progress_bar("Downloading second script...", 5)

    system_info = collect_pc_info()

    save_info_to_file(system_info)

    display_github_message()

if __name__ == "__main__":
    main()
