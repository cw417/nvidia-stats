#   TODO:
#     - Add functioning close button to make_chart
#     - replace get_data calls with run_command and format_num

import subprocess
import re
import csv
import time
import pandas as pd
import settings

time_elapsed = 0

def run_command(cmd):
    """Runs string cmd in OS shell, return string output"""
    return str(subprocess.check_output(cmd, shell=True))

def format_num(regex, string_to_check):
    """
    Take in string regex and string string_to_check, return formatted string number.
    Regex is appended to "\d+" before being compiled.
    
    """
    reg = re.compile(rf"\d+{regex}")
    match  = reg.search(string_to_check).group(0)
    return match.strip(regex)

def get_data(cmd, reg_addition):
    """Takes in string command, string addition to regex pattern, and string to strip"""
    check = str(subprocess.check_output(cmd, shell=True))
    regex = re.compile(rf"\d+{reg_addition}")
    match  = regex.search(check).group(0)
    return match.strip(reg_addition)
    
def gpu_temp():
    """Returns current GPU temperature"""
    return get_data('nvidia-smi --query-gpu=temperature.gpu --format=csv', "")
    

def gpu_use():
    """Returns current GPU percent use"""
    return get_data("nvidia-smi --query-gpu=utilization.gpu --format=csv", " %")
    

def gpu_clock():
    """Returns current GPU clock"""
    return get_data("nvidia-smi --query-gpu=clocks.gr --format=csv", " MHz")
    

def vram_use():
    """Returns current GPU VRAM percent use"""
    return get_data("nvidia-smi --query-gpu=utilization.memory --format=csv", " %")

def vram_clock():
    """Returns current GPU VRAM clock"""
    return get_data("nvidia-smi --query-gpu=clocks.mem --format=csv", " MHz")

def fan_speed():
    """Returns current fan speed"""
    return get_data("nvidia-smi --query-gpu=fan.speed --format=csv", " %")

def get_total(col):
    """Takes in string column name, returns float average"""
    df = pd.read_csv('nvidia_stats.csv')
    data = df[col]
    avg = data.mean(axis=0)
    return avg

def print_formatted():
    """Prints formatted data"""
    print(f'GPU Temp:   {gpu_temp()} C,        avg={round(get_total("gpu_temp"), 2)}')
    print(f'GPU Use:    {gpu_use()} %,        avg={round(get_total("gpu_use"), 2)}')
    print(f'GPU Clock:  {gpu_clock()} MHz,    avg={round(get_total("gpu_clock"), 2)}')
    print(f'VRAM Use:   {vram_use()} %,        avg={round(get_total("vram_use"), 2)}')
    print(f'VRAM Clock: {vram_clock()} MHz,    avg={round(get_total("vram_clock"), 2)}')
    print(f'Fan Speed:  {fan_speed()} %,        avg={round(get_total("fan_speed"), 2)}')

def write_csv_header():
    """Writes initial csv file for data"""
    with open('nvidia_stats.csv', 'w') as fp:
        fieldnames = ['time_elapsed', 'gpu_temp', 'gpu_use', 'gpu_clock', 'vram_use', 'vram_clock', 'fan_speed']
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()

def write_csv():
    """Writes data csv file"""
    with open('nvidia_stats.csv', 'a') as fp:
        writer = csv.writer(fp)
        writer.writerow([time_elapsed, gpu_temp(), gpu_use(), gpu_clock(), vram_use(), vram_clock(), fan_speed()])

def increment():
    """Increments global timer"""
    global time_elapsed
    time_elapsed += settings.update_time 
    time.sleep(settings.update_time)

def get_stats():
    """Prints stats to terminal"""
    #print_formatted()
    #print("\n\n")
    write_csv()

def main():
    """Writes csv and starts main loop"""
    write_csv_header()
    while True:
        get_stats()
        increment()

if __name__ == '__main__':
    cmd = run_command("nvidia-smi --query-gpu=temperature.gpu --format=csv")
    print(format_num("", cmd))

    #main()