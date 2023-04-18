import socket
from pickle import dumps,loads
import threading
def message_from_client():
    global connection,connected
    while(connected):
        data=connection.recv(1024)
        print("MESSAGE FROM THE CLIENT SIR : ",loads(data))
x=socket.socket()
host='127.0.0.1'
port=5000
x.bind((host,port))
x.listen(5)
connection,address=x.accept()
connected=True
#message_from_client()
client_thread=threading.Thread(target=message_from_client())
client_thread.start()