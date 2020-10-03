import time
import zmq
import threading
import numpy as np
'''Server'''
def Spectogram_Image_Listener():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    while True:
        message = socket.recv()
        print("Recieved request")
        print(np.fromstring(message, dtype=int))
        print(message)
        time.sleep(1)
        socket.send(b"Hello")


def Histplot_Listener():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")
    while True:
        message = socket.recv()
        print("Recieved request")
        time.sleep(1)

t1 = threading.Thread(target=Spectogram_Image_Listener, args=())
t2 = threading.Thread(target=Histplot_Listener, args=())
t1.start()
t2.start()
t1.join()
t2.join()

#context = zmq.Context()
#socket = context.socket(zmq.REP)
#socket.bind("tcp://*:5555")
#
#while True:
#    message = socket.recv_multipart()
#    print ("Recieved request: %s" %message)
#    time.sleep(1)
#    socket.send_multipart([b"World", b"Hello"])