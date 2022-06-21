import stats
import graph
import chart
import threading
import time
import settings

def main():
    stats_thread = threading.Thread(target=stats.main).start()
    time.sleep(settings.start_time) # sleep is needed to give app time to write to csv so make_graph can have iloc for setting ax#.text variable
    graph_thread = threading.Thread(target=graph.main).start()
    chart_thread = threading.Thread(target=chart.main).start()

if __name__ == "__main__":
    main()