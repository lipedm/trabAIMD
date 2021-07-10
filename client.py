import socket
import time
import random

host = '172.31.16.25'
port = 6006


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (host, port)
sock.settimeout(1)
cwnd = 1

try:
	for i in range(1, 30):
		start = time.time()
		message = random.random
		try:
			sent = sock.sendto(message.encode("utf-8"), server_addr)
			print("Sent " + message)
			data, server = sock.recvfrom(cwnd)
			print("Received " + data.decode("utf-8"))
			end = time.time();
			elapsed = end - start
			cwnd = cwnd^2
			print("RTT: " + str(elapsed) + " seconds\n")

		except socket.timeout:
			print("#" + str(i) + " Requested Time out\n")
			print("#" + str(i) + " Congestion Detected\n")
			cwnd = int(cwnd / 2)

finally:
	print("closing socket")
	sock.close()