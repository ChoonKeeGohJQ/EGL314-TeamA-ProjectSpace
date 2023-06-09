import socket

TCP_IP='192.168.10.10'
TCP_PORT=5005
BUFFER_SIZE=1024

# Buttons 1-9 (Turns on O)
# Buttons 10-18 (Turns on X)
# Buttons 19-27 (Turns off O)
# Buttons 28-36 (Turns off X)

A = [
b"TCPSend(1,'{wdcustomscriptclick(19)}')!",
b"TCPSend(1,'{wdcustomscriptclick(20)}')!",
b"TCPSend(1,'{wdcustomscriptclick(21)}')!",
b"TCPSend(1,'{wdcustomscriptclick(22)}')!",
b"TCPSend(1,'{wdcustomscriptclick(23)}')!",
b"TCPSend(1,'{wdcustomscriptclick(24)}')!",
b"TCPSend(1,'{wdcustomscriptclick(25)}')!",
b"TCPSend(1,'{wdcustomscriptclick(26)}')!",
b"TCPSend(1,'{wdcustomscriptclick(27)}')!"
    ]	#Lines for turning off O

B = [
b"TCPSend(1,'{wdcustomscriptclick(28)}')!",
b"TCPSend(1,'{wdcustomscriptclick(29)}')!",
b"TCPSend(1,'{wdcustomscriptclick(30)}')!",
b"TCPSend(1,'{wdcustomscriptclick(31)}')!",
b"TCPSend(1,'{wdcustomscriptclick(32)}')!",
b"TCPSend(1,'{wdcustomscriptclick(33)}')!",
b"TCPSend(1,'{wdcustomscriptclick(34)}')!",
b"TCPSend(1,'{wdcustomscriptclick(35)}')!",
b"TCPSend(1,'{wdcustomscriptclick(36)}')!"
    ]	#Lines for turning off X
C = [
b"TCPSend(1,'{wdcustomscriptclick(38)}')!",
b"TCPSend(1,'{wdcustomscriptclick(40)}')!"
    ]   #Lines for turning off winner sign

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

for x in A:
    s.send(x)	#Turns all O off
    
for x in B:
    s.send(x)	#Turns all X off
    
for x in C:
    s.send(x)	#Turns all winner signs off
    
data=s.recv(BUFFER_SIZE)
s.close()
print("Received data : %s"%data)
