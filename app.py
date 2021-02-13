# WORKFLOW:
#     - specify command to get GPU stats
#     - run command with subprocess.check_output
#     - parse output with regex
#     - output regex match to csv file
#     - create real time graph with matplotlib - make_graph.py
#   TODO:
#     - Run app & make_graph simultaneously from one program

import subprocess
import re
import csv
import time
import pandas as pd

time_elapsed = 0

def gpu_temp():
    cmd = 'nvidia-smi --query-gpu=temperature.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+')
    match  = reg.search(check).group(0)
    return match

def gpu_use():
    cmd = 'nvidia-smi --query-gpu=utilization.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ %')
    match  = reg.search(check).group(0)
    num = match.strip(' %')
    return num

def gpu_clock():
    cmd = 'nvidia-smi --query-gpu=clocks.gr --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ MHz')
    match  = reg.search(check).group(0)
    num = match.strip(' MHz')
    return num

def vram_use():
    cmd = 'nvidia-smi --query-gpu=utilization.memory --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ %')
    match  = reg.search(check).group(0)
    num = match.strip(' %')
    return num

def vram_clock():
    cmd = 'nvidia-smi --query-gpu=clocks.mem --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d+ MHz')
    match  = reg.search(check).group(0)
    num = match.strip(' MHz')
    return num

def fan_speed():
    cmd = 'nvidia-smi --query-gpu=fan.speed --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d* %')
    match  = reg.search(check).group(0)
    num = match.strip(' %')
    return num

def get_total(col):
    df = pd.read_csv('nvidia_stats.csv')
    data = df[col]
    avg = data.mean(axis=0)
    return avg

def print_formatted():
    print(f'GPU Temp:   {gpu_temp()} C,        avg={round(get_total("gpu_temp"), 2)}')
    print(f'GPU Use:    {gpu_use()} %,        avg={round(get_total("gpu_use"), 2)}')
    print(f'GPU Clock:  {gpu_clock()} MHz,    avg={round(get_total("gpu_clock"), 2)}')
    print(f'VRAM Use:   {vram_use()} %,        avg={round(get_total("vram_use"), 2)}')
    print(f'VRAM Clock: {vram_clock()} MHz,    avg={round(get_total("vram_clock"), 2)}')
    print(f'Fan Speed:  {fan_speed()} %,        avg={round(get_total("fan_speed"), 2)}')

def write_csv_header():
    with open('nvidia_stats.csv', 'w') as fp:
        fieldnames = ['time_elapsed', 'gpu_temp', 'gpu_use', 'gpu_clock', 'vram_use', 'vram_clock', 'fan_speed']
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()

def write_csv():
    with open('nvidia_stats.csv', 'a') as fp:
        writer = csv.writer(fp)
        writer.writerow([time_elapsed, gpu_temp(), gpu_use(), gpu_clock(), vram_use(), vram_clock(), fan_speed()])

def increment():
    global time_elapsed
    time_elapsed += 2
    time.sleep(2)

def get_stats():
    print_formatted()
    print("\n\n")
    write_csv()

def main():
    write_csv_header()
    while True:
        get_stats()
        increment()

if __name__ == '__main__':
    main()