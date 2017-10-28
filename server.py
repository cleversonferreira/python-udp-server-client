import socket
import struct
import random

HOST = ''
UDP_PORT = 8805

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((HOST, UDP_PORT))

print("waiting for messages ...")

while True:
    data, addr = sock.recvfrom(1024)
    print "\n---> new message"
    print "ip: [", addr[0].strip(),"]"
    print "port: [",addr[1], "]"
    print "body: [", data, "]"
    print("sending answer ...")
    sock.sendto('opa', (addr[0].strip(), 8805))