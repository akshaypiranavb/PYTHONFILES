import socket
from pickle import dumps,loads
x=socket.socket()
host='127.0.0.1'
port=5000
x.connect((host,port))
while(True):
    data=input("ENTER A MESSAGE CLIENT SIR : ")
    x.sendall(dumps(data))