import socket #nutshell communication link
x=socket.socket()
port=5000
host='127.0.0.1'
x.bind((host,port))
x.listen(5)
connection,address=x.accept()
print("CONNECTED WITH OUR CLIENT",(connection,address))
x.close()
