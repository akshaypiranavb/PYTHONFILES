#sending data between sockets
import socket
from pickle import *
x=socket.socket()
port=50000
host='127.0.0.1'
x.connect((host,port))
data=dumps("IM AKSHAY PIRANAV ")
x.sendall(data)
#x.sendall(b'AKSHAY ')
#x.send(b'HELLO IM AKSHAY',1024)