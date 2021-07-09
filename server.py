import socket

udp_ip = "172.31.16.25"
udp_port = 6006
buffer = 64

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))


while True:
    data, addr = sock.recvfrom(buffer)
    print("mensagem recebida: %s" % data)
    print(addr)
    sendBack = data
    sock.sendto(sendBack,addr)