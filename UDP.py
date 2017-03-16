import socket
import time


UDP_IP = "localhost"
UDP_PORT = 80


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print "Socket binded\n"
while True:
    data, addr = sock.recvfrom(1024)
    print data
    
