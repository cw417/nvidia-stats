# WORKFLOW:
#     - specify command to get GPU stats
#     - run command with subprocess.check_output
#     - parse output with regex
#   TODO:
#     - output regex match to csv file
#     - convert csv to real time graph with matplotlib


import subprocess
import re

def get_GPU_temp():
    cmd = 'nvidia-smi --query-gpu=temperature.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d\d')
    match  = reg.search(check).group(0)
    print(f'GPU Temp: {match} C')

def get_GPU_utilization():
    cmd = 'nvidia-smi --query-gpu=utilization.gpu --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d* %')
    match  = reg.search(check).group(0)
    print(f'GPU Use: {match}')

def get_GPU_clock():
    cmd = 'nvidia-smi --query-gpu=clocks.gr --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d\d\d\d MHz')
    match  = reg.search(check).group(0)
    print(f'GPU Clock: {match}')

def get_VRAM_utilization():
    cmd = 'nvidia-smi --query-gpu=utilization.memory --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d* %')
    match  = reg.search(check).group(0)
    print(f'VRAM Use: {match}')

def get_VRAM_clock():
    cmd = 'nvidia-smi --query-gpu=clocks.mem --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d\d\d\d MHz')
    match  = reg.search(check).group(0)
    print(f'VRAM Clock: {match}')

def get_fan_speed():
    cmd = 'nvidia-smi --query-gpu=fan.speed --format=csv'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.compile(r'\d* %')
    match  = reg.search(check).group(0)
    print(f'Fan Speed: {match}')

if __name__ == '__main__':
    get_GPU_utilization()
    get_GPU_clock()
    get_VRAM_utilization()
    get_VRAM_clock()
    get_fan_speed()
    get_GPU_temp()