import socket
import time
import random
import string

host = '172.31.16.25'
port = 6006


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (host, port)
sock.settimeout(1)
cwnd = 1
letters = string.ascii_lowercase

try:
	for i in range(1, 30):
		start = time.time()
		message = ''.join(random.choice(letters) for i in range(10))
		try:
			sent = sock.sendto(message.encode("utf-8"), server_addr)
			print("Sent " + message)
			data, server = sock.recvfrom(cwnd)
			print("Received " + data.decode("utf-8"))
			end = time.time();
			elapsed = end - start
			cwnd += cwnd*cwnd
			print("RTT: " + str(elapsed) + " seconds\n")
			print("cwnd agora:" + str(cwnd) + "\n")

		except socket.timeout:
			print("#" + str(i) + " Requested Time out\n")
			print("#" + str(i) + " Congestion Detected\n")
			cwnd = int(cwnd / 2)
			print("cwnd agora:" + str(cwnd) + "\n")

finally:
	print("closing socket")
	sock.close()