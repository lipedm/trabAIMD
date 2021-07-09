import socket

udp_ip = "172.31.16.25"
udp_port = 6006

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))


while True:
    data, addr = sock.recvfrom(4096)
    print("mensagem recebido: %s" % data)
    print(addr)
    if (data.decode("utf-8") == "exit"):
        break
    sendBack = data.decode("utf-8")
    sock.sendto(sendBack.encode("utf-8"),addr)