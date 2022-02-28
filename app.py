#   TODO:
#     - Add functioning close button to make_chart

import subprocess
import re
import csv
import time
import pandas as pd

time_elapsed = 0

def get_data(cmd, reg_addition):
    """Takes in string command, string addition to regex pattern, and string to strip"""
    check = str(subprocess.check_output(cmd, shell=True))
    regex = re.compile(rf"\d+{reg_addition}")
    match  = regex.search(check).group(0)
    return match.strip(reg_addition)
    


def gpu_temp():
    """Checks current GPU temperature"""
    return get_data('nvidia-smi --query-gpu=temperature.gpu --format=csv', "", "")
    """ cmd = 'nvidia-smi --query-gpu=temperature.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+')
    match  = reg.search(check).group(0)
    return match """

def gpu_use():
    """Checks current GPU percent use"""
    return get_data("nvidia-smi --query-gpu=utilization.gpu --format=csv", " %"," %")
    """ cmd = 'nvidia-smi --query-gpu=utilization.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ %')
    match  = reg.search(check).group(0)
    num = match.strip(' %')
    return num """

def gpu_clock():
    """Checks current GPU clock"""
    return get_data("nvidia-smi --query-gpu=clocks.gr --format=csv", " MHz")
    """ cmd = 'nvidia-smi --query-gpu=clocks.gr --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ MHz')
    match  = reg.search(check).group(0)
    num = match.strip(' MHz')
    return num """

def vram_use():
    """Checks current GPU VRAM percent use"""
    return get_data("nvidia-smi --query-gpu=utilization.memory --format=csv", " %")
    """ cmd = 'nvidia-smi --query-gpu=utilization.memory --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ %')
    match  = reg.search(check).group(0)
    num = match.strip(' %') 
    return num """

def vram_clock():
    """Checks current GPU VRAM clock"""
    return get_data("nvidia-smi --query-gpu=clocks.mem --format=csv", " MHz")
    """ cmd = 'nvidia-smi --query-gpu=clocks.mem --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ MHz')
    match  = reg.search(check).group(0)
    num = match.strip(' MHz')
    return num """

def fan_speed():
    """Checks current fan speed"""
    return get_data("nvidia-smi --query-gpu=fan.speed --format=csv", " %")
    """ cmd = 'nvidia-smi --query-gpu=fan.speed --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d* %')
    match  = reg.search(check).group(0)
    num = match.strip(' %')
    return num """

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
    time_elapsed += 2
    time.sleep(2)

def get_stats():
    """Prints stats to terminal"""
    print_formatted()
    print("\n\n")
    write_csv()

def main():
    """Writes csv and starts main loop"""
    write_csv_header()
    while True:
        get_stats()
        increment()

if __name__ == '__main__':
    main()