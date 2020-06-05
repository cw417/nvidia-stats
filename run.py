import app
import make_graph
import threading

def main():
    app_thread = threading.Thread(target=app.run).start()
    graph_thread = threading.Thread(target=make_graph.run).start()

if __name__ == "__main__":
    main()