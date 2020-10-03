import zmq
import numpy as np
from numpy import zeros, ones, log10, array
context = zmq.Context()

print ("Connecting to HelloWorld Server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    byteString_2DSpectogram = np.array([1, 2, 3, 4, 5, 6]).tostring()
    print("Sending request %s ..." % request)
    socket.send(byteString_2DSpectogram)
    message = socket.recv()
    print (message)