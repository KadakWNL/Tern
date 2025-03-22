import threading
from backend import server

if __name__ == "__main__":
        # Start the server in a separate thread
    server_thread = threading.Thread(target=server.main, daemon=True)
    server_thread.start()
    from backend import work_GUI_PT2


