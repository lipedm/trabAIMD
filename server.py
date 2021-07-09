import random
from socket import *


host = '172.31.16.25'
port = 6006

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((host, port))
print("Started UDP server on port %d" % port)
while True:

    rand = random.randint(0, 10)

    message, address = serverSocket.recvfrom(1024)

    message = message.upper()

    if rand < 4:
        continue

    serverSocket.sendto(message, address)