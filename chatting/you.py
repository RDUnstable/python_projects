import socket
import os
import sys


host = "192.168.56.1"
port = 9997

def server_connect():
    global host
    global port
    global s

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))

    except socket.error as err:
        print("Could not connect :(.............he/she is offline :(")
        sys.exit()

def send_message():
    global host
    global port
    global s
 

    
    msg = input("Enter reply: ")
    if msg == "exit":
        sys.exit()
            
    s.send(str.encode(msg,"utf-8"))

def receive_message():
    global host
    global port
    global s

    data = s.recv(1024)
    print("Reply: " + data.decode("utf-8"))


server_connect()

while True:
    ch = input("Send or receive?(s/r): ")
    if ch == "exit":
        sys.exit()

    elif ch == 's':
        send_message()

    elif ch == 'r':
        receive_message()
