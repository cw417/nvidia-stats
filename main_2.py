import chart
import graph
import settings
import stats
import threading
import time

def get_user_info():
  run_chart = input("Show stats chart? (y/n) ")
  run_graph = input("Show graphs? (y/n) ")
  return run_chart, run_graph

def main(run_chart, run_graph):
  stats_thread = threading.Thread(target=stats.main).start()
  time.sleep(settings.start_time) # sleep is needed to give app time to write to csv so make_graph can have iloc for setting ax#.text variable
  if run_chart != "n":
    chart_thread = threading.Thread(target=chart.main).start()
  if run_graph != "n":
    graph_thread = threading.Thread(target=graph.main).start()

if __name__ == "__main__":
  info = get_user_info()
  main(info[0], info[1])