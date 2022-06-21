import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import re
import subprocess
from matplotlib.animation import FuncAnimation
import settings


def max_clock():
    # Get data for max GPU clock to later set GPU clock graph axis limit
    cmd = 'nvidia-smi -q | grep Video'
    check = str(subprocess.check_output(cmd, shell=True))
    reg = re.findall("\d+", check)
    return int(reg[1])

max_clock = max_clock()

def main():

  style.use('seaborn')

  fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True)

  def animate(i):

    # Read data from CSV  
    data = pd.read_csv('nvidia_stats.csv')
    time = data['time_elapsed']
    gpu_temp = data['gpu_temp']
    gpu_clock = data['gpu_clock']
    gpu_use = data['gpu_use']
    fan_speed = data['fan_speed']

    # temp
    ax1.cla()
    ax1.set_ylim([0,100])
    ax1.plot(time, gpu_temp, label='GPU Temp', color='red')
    ax1.legend(loc='upper left')
    ax1.set_title('GPU Stats') # displays as graph title since this graph is at the top
    ax1.text(time.iloc[-1], 100, f'GPU Temp: {gpu_temp.iloc[-1]}\u00b0', horizontalalignment='right', verticalalignment='bottom')

    # clock
    ax2.cla()
    ax2.set_ylim([0,max_clock])
    ax2.plot(time, gpu_clock, label='GPU Clock', color='blue')
    ax2.legend(loc='upper left')
    ax2.text(time.iloc[-1], max_clock, f'GPU Clock: {gpu_clock.iloc[-1]} Mhz', horizontalalignment='right', verticalalignment='bottom')

    # use
    ax3.cla()
    ax3.set_ylim([0,100])
    ax3.plot(time, gpu_use, label='GPU Use', color='green')
    ax3.legend(loc='upper left')
    ax3.text(time.iloc[-1], 100, f'GPU Use: {gpu_use.iloc[-1]}%', horizontalalignment='right', verticalalignment='bottom')

    # fan
    ax4.cla()
    ax4.set_ylim([0,100])
    ax4.plot(time, fan_speed, label='Fan Speed', color='black')
    ax4.legend(loc='upper left')
    ax4.set_xlabel('Time')
    ax4.text(time.iloc[-1], 100, f'Fan speed: {fan_speed.iloc[-1]}%', horizontalalignment='right', verticalalignment='bottom')

    #plt.tight_layout()

  ani = FuncAnimation(fig, animate, interval=settings.update_time_ms)

  plt.show()

if __name__ == '__main__':
    main()