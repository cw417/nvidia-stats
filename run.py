import app
import make_graph
import threading
import time

def main():
    app_thread = threading.Thread(target=app.run).start()
    time.sleep(4) # sleep is needed to give app time to write to csv so make_graph can have iloc for setting ax#.text variable
    graph_thread = threading.Thread(target=make_graph.run).start()

if __name__ == "__main__":
    main()