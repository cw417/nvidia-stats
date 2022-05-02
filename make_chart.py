import tkinter as tk
import pandas as pd
import time
import settings

class StatsGraph(tk.Frame):
  def __init__(self, master=None, *args, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.data = pd.read_csv('nvidia_stats.csv')

    self.master.title("Nvidia Stats")

    # Grid item settings
    label_width = 12
    label_font = ("Helvetica", 16)
    num_width = 10
    num_font = ("Helvetica", 16)

    data = pd.read_csv('nvidia_stats.csv')
    gpu_temp = data['gpu_temp']
    gpu_clock = data['gpu_clock']
    gpu_use = data['gpu_use']
    vram_use = data['vram_use']
    vram_clock = data['vram_clock']
    fan_speed = data['fan_speed']


    # Create labels
    gpu_temp_label = tk.Label(self, width=label_width, text="GPU temp: ", anchor='e')
    gpu_use_label = tk.Label(self, width=label_width, text="GPU use: ", anchor='e')
    gpu_clock_label = tk.Label(self, width=label_width, text="GPU clock: ", anchor='e')
    vram_use_label = tk.Label(self, width=label_width, text="VRAM use: ", anchor='e')
    vram_clock_label = tk.Label(self, width=label_width, text="VRAM clock: ", anchor='e')
    fan_speed_label = tk.Label(self, width=label_width, text="Fan speed: ", anchor='e')

    gpu_temp_label.configure(font=label_font)
    gpu_use_label.configure(font=label_font)
    gpu_clock_label.configure(font=label_font)
    vram_use_label.configure(font=label_font)
    vram_clock_label.configure(font=label_font)
    fan_speed_label.configure(font=label_font)

    gpu_temp_label.grid(row=0, column=0, sticky='w')
    gpu_use_label.grid(row=1, column=0, sticky='w')
    gpu_clock_label.grid(row=2, column=0, sticky='w')
    vram_use_label.grid(row=3, column=0, sticky='w')
    vram_clock_label.grid(row=4, column=0, sticky='w')
    fan_speed_label.grid(row=5, column=0, sticky='w')

    # Create numbers
    self.gpu_temp_num = tk.Label(self, width=num_width, text=f"{gpu_temp.iloc[-1]}\u00b0", anchor='w')
    self.gpu_use_num = tk.Label(self, width=num_width, text=f"{gpu_use.iloc[-1]} \u0025", anchor='w')
    self.gpu_clock_num = tk.Label(self, width=num_width, text=f"{gpu_clock.iloc[-1]} Mhz", anchor='w')
    self.vram_use_num = tk.Label(self, width=num_width, text=f"{vram_use.iloc[-1]} \u0025", anchor='w')
    self.vram_clock_num = tk.Label(self, width=num_width, text=f"{vram_clock.iloc[-1]} Mhz", anchor='w')
    self.fan_speed_num = tk.Label(self, width=num_width, text=f"{fan_speed.iloc[-1]} \u0025", anchor='w')

    self.gpu_temp_num.configure(font=num_font)
    self.gpu_use_num.configure(font=num_font)
    self.gpu_clock_num.configure(font=num_font)
    self.vram_use_num.configure(font=num_font)
    self.vram_clock_num.configure(font=num_font)
    self.fan_speed_num.configure(font=num_font)

    self.gpu_temp_num.grid(row=0, column=1, sticky='w')
    self.gpu_use_num.grid(row=1, column=1, sticky='w')
    self.gpu_clock_num.grid(row=2, column=1, sticky='w')
    self.vram_use_num.grid(row=3, column=1, sticky='w')
    self.vram_clock_num.grid(row=4, column=1, sticky='w')
    self.fan_speed_num.grid(row=5, column=1, sticky='w')


    def get_data():
      #Get data
      data = pd.read_csv('nvidia_stats.csv')
      gpu_temp = data['gpu_temp']
      gpu_clock = data['gpu_clock']
      gpu_use = data['gpu_use']
      vram_use = data['vram_use']
      vram_clock = data['vram_clock']
      fan_speed = data['fan_speed']
      return [gpu_temp, gpu_use, gpu_clock, vram_use, vram_clock, fan_speed]

    def update_gpu_temp_num():
      updated_data = get_data()
      updated = updated_data[0].iloc[-1]
      self.gpu_temp_num.configure(text=f"{updated}\u00b0")
      self.gpu_temp_num.after(settings.update_time_ms, update_gpu_temp_num)

    def update_gpu_use_num():
      updated_data = get_data()
      updated = updated_data[1].iloc[-1]
      self.gpu_use_num.configure(text=f"{updated} \u0025")
      self.gpu_use_num.after(settings.update_time_ms, update_gpu_use_num)

    def update_gpu_clock_num():
      updated_data = get_data()
      updated = updated_data[2].iloc[-1]
      self.gpu_clock_num.configure(text=f"{updated} Mhz")
      self.gpu_clock_num.after(settings.update_time_ms, update_gpu_clock_num)

    def update_vram_use_num():
      updated_data = get_data()
      updated = updated_data[3].iloc[-1]
      self.vram_use_num.configure(text=f"{updated} \u0025")
      self.vram_use_num.after(settings.update_time_ms, update_vram_use_num)

    def update_vram_clock_num():
      updated_data = get_data()
      updated = updated_data[4].iloc[-1]
      self.vram_clock_num.configure(text=f"{updated} Mhz")
      self.vram_clock_num.after(settings.update_time_ms, update_vram_clock_num)

    def update_fan_speed_num():
      updated_data = get_data()
      updated = updated_data[5].iloc[-1]
      self.fan_speed_num.configure(text=f"{updated} \u0025")
      self.fan_speed_num.after(settings.update_time_ms, update_fan_speed_num)

    self.gpu_temp_num.after(settings.update_time_ms, update_gpu_temp_num)
    self.gpu_use_num.after(settings.update_time_ms, update_gpu_use_num)
    self.gpu_clock_num.after(settings.update_time_ms, update_gpu_clock_num)
    self.vram_use_num.after(settings.update_time_ms, update_vram_use_num)
    self.vram_use_num.after(settings.update_time_ms, update_vram_clock_num)
    self.fan_speed_num.after(settings.update_time_ms, update_fan_speed_num)

def main():
  root = tk.Tk()
  app = StatsGraph(root)
  app.pack(fill=tk.BOTH, expand=1)
  root.mainloop()

if __name__ == '__main__':
  main()