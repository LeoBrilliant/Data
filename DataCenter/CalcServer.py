'''
Created on 20160606

@author: user
'''

import zmq
import time
import json

context = zmq.Context()

# subscriber = context.socket(zmq.SUBSCRIBE)

socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

#orderContext = zmq.Context()

orderSocket = context.socket(zmq.REQ)

n = orderSocket.connect("tcp://localhost:5556")
# print(orderSocket)
# print(n)

msgCounter = 0

while True:
    message = socket.recv()
    
    msg = str(message)
#     msg = json.decoder(message)
    msg = json.dumps(message)
    print("Request: %s" % message)
    print("Request: %s" % msg)
    
    print("Received request %d: %s" % (msgCounter, msg))
    
    msgCounter += 1
    
    orderSocket.send(message)
    
    time.sleep(1)
    
    message = orderSocket.recv()
    
    print("Reply: %s" % message)
    
    socket.send(b"World")
    


