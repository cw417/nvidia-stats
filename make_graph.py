import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from matplotlib.animation import FuncAnimation

def run():

    style.use('fivethirtyeight')

    def animate(i):
        data = pd.read_csv('nvidia_stats.csv')
        x = data['time_elapsed']
        y = data['GPU_temp']

        plt.cla()
        plt.plot(x, y)

    ani = FuncAnimation(plt.gcf(), animate, interval=2000)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    run()