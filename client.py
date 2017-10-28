# import libs
import socket
import struct

# define vars
# UDP_PORT = 8805
# UDP_IP = "2804:7f4:3b80:c6e8:74b4:f882:c739:a101"
HOST = ''
UDP_PORT = 8805
UDP_IP = "2804:7f4:3b80:c6e8:212:4b00:f28:af80"
LED_TOGGLE_REQUEST = (0x79)
MESSAGE = struct.pack(">B", LED_TOGGLE_REQUEST)

#send message
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((HOST, UDP_PORT))
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)

#receive message
print "\n---> callback received"
print "ip: [", addr[0].strip(),"]"
print "port: [",addr[1], "]"
print "body: [", data, "]"