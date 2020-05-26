# NvidiaStats
Nvidia GPU stat reporting app for Linux

## Table of Contents
1. About
2. Getting Started
    1. Prerequisites
    2. Installing
3. How It Works

## About
NvidiaStats is a command line GPU stat reporting application written for use in a Linux-based operating system running the Xorg display server with proprietary Nvidia drivers. Currently, it will report GPU utilization, GPU clock, GPU temperature, VRAM utilization, VRAM clock, and fan speed.

## Getting Started
### Prerequisites
- Python 3.6+
- Linux-based operating system
    - Xorg display server
- Nvidia GPU running proprietary nvidia drivers

### Installing
1) Clone the repository: `git clone https://github.com/cw417/NvidiaStats`
2) Ensure you are using prorietary drivers compatible with the NvidiaStats:
    - `cat /etc/X11/xorg.conf | grep nvidia-xconfig`
    - If this returns an output, you are using proprietary Nvidia drivers
3) Run NvidiaStats: 
    - Change directory into the cloned NvidiaStats directory: `cd NvidiaStats`
    - Run the app: `python app.py`

## How It Works
 - GPU stats are obtained via the subprocess module running the `nvidia-smi -q` command with the specified stat output option
 - Output from the subprocess module is parsed via regex
 - The regex match output is formatted and printed to the command line