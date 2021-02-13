import app
import make_graph
import make_chart
import threading
import time

def main():
    app_thread = threading.Thread(target=app.main).start()
    time.sleep(2) # sleep is needed to give app time to write to csv so make_graph can have iloc for setting ax#.text variable
    graph_thread = threading.Thread(target=make_graph.main).start()
    chart_thread = threading.Thread(target=make_chart.main).start()

if __name__ == "__main__":
    main()