import data
import server
import threading

PORT=8000

def go():
    #hosting server
    hosting_thread = threading.Thread(target=hostthread, args=() )
    hosting_thread.daemon = True
    hosting_thread.start()

    #other activities

def hostthread():
    server.serve()

def init():
    data.try_generate_identity()
