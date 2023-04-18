#sending data between sockets
import socket
from pickle import *
x=socket.socket()
port=50000
host='127.0.0.1'
x.bind((host,port))
x.listen(5)
connection,address=x.accept()
print("CONNECTED WITH OUR CLIENT ",(connection,address))
data=connection.recv(1024)
data=loads(data)
print("MESSAGE FROM CLIENT SERVER : ",data)
x.close()