#sender side

import socket
mypp=socket.SOCK_DGRAM
afnn=socket.AF_INET
s=socket.socket(afnn,mypp)
s.sendto("heii".encode(),("192.168.43.105",5364))
