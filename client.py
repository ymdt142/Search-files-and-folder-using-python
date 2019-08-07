import socket
host="192.168.0.191"
port=9999
s=socket.socket()
s.connect((host,port))
message=input(">-")
while message!="q":
	s.send(message.encode("utf-8"))
	data=s.recv(1024).decode("utf-8")
	print("receivd:- "+data)
	message=input(">-")
s.close()