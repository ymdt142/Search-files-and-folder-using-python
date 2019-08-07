import socket
import sys
def socket_create():
    global s
    s=socket.socket()
def Bind():
    global s
    host='192.168.0.110'
    s.bind((host,999))
    s.listen(1)
    print("binded and listning")
def connect():
    global s
    c, addr=s.accept()
    print("connection established"+ str(addr))
    send_command(c)
    conn.close()
def send_command(conn):
    while True:
        data=c.recv(1024).decode('utf-8')
        if not data:
            break
        print("from client"+data)
        data=data.upper()
        print("sending:- "+data)
        c.send(data.encode('utf-8'))
def main():
    socket_create()
    Bind()
    connect()
main()
