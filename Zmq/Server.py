'''
Created on 20160606

@author: user
'''

import zmq
import time

context = zmq.Context()

# subscriber = context.socket(zmq.SUBSCRIBE)

socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print("Received request: %s" % message)
    
    time.sleep(1)
    
    socket.send(b"World")
    


