import socket
import sys

host = '172.31.16.25'
port = 6006
buffer = 64

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Falha ao bindar o socket')
	sys.exit()

while True:
	msg = input("insira sua mensagem: ")
	try :		
		sock.sendto(msg.encode('utf-8'), (host, port))
		reply = sock.recvfrom(buffer)
		print(reply)
		print("mensagem recebido: %d" % buffer) 
		serverInfo = reply[1][0]
		replyDecoded = reply[0].decode("utf-8")

		print("informações do servidor %s recebidas com sucesso" % serverInfo)
		print(replyDecoded)

		if (replyDecoded == False):
			break
	except socket.error as msg:
		print ('Error Code : ') + str(msg[0]) + ' Mensagem ' + msg[1]
		sys.exit()