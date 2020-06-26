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

def GPU_temp():
    cmd = 'nvidia-smi --query-gpu=temperature.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d\d')
    match  = reg.search(check).group(0)
    return match

def GPU_use():
    cmd = 'nvidia-smi --query-gpu=utilization.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d* %')
    match  = reg.search(check).group(0)
    num = match.strip(' %')
    return num

def GPU_clock():
    cmd = 'nvidia-smi --query-gpu=clocks.gr --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d\d\d\d MHz')
    match  = reg.search(check).group(0)
    num = match.strip(' MHz')
    return num

def VRAM_use():
    cmd = 'nvidia-smi --query-gpu=utilization.memory --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d* %')
    match  = reg.search(check).group(0)
    num = match.strip(' %')
    return num

def VRAM_clock():
    cmd = 'nvidia-smi --query-gpu=clocks.mem --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d\d\d\d MHz')
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
    print(f'GPU Temp:   {GPU_temp()} C,        avg={get_total("GPU_temp")}')
    print(f'GPU Use:    {GPU_use()} %,        avg={get_total("GPU_use")}')
    print(f'GPU Clock:  {GPU_clock()} MHz,    avg={get_total("GPU_clock")}')
    print(f'VRAM Use:   {VRAM_use()} %,        avg={get_total("VRAM_use")}')
    print(f'VRAM Clock: {VRAM_clock()} MHz,    avg={get_total("VRAM_clock")}')
    print(f'Fan Speed:  {fan_speed()} %,        avg={get_total("fan_speed")}')

def write_csv_header():
    with open('nvidia_stats.csv', 'w') as fp:
        fieldnames = ['time_elapsed', 'GPU_temp', 'GPU_use', 'GPU_clock', 'VRAM_use', 'VRAM_clock', 'fan_speed']
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()

def write_csv():
    with open('nvidia_stats.csv', 'a') as fp:
        writer = csv.writer(fp)
        writer.writerow([time_elapsed, GPU_temp(), GPU_use(), GPU_clock(), VRAM_use(), VRAM_clock(), fan_speed()])

def increment():
    global time_elapsed
    time_elapsed += 2
    time.sleep(2)


def get_stats():
    print_formatted()
    print("\n\n")
    write_csv()

def run():
    write_csv_header()
    while True:
        get_stats()
        increment()

if __name__ == '__main__':
    run()