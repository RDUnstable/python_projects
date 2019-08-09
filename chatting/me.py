import socket
import os
import sys


host = "192.168.56.1"
port = 9997


def create_socket():
    global host
    global port
    global s

    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Server created successfully............")
        
    except socket.error as err:
        print("Not created..........")
        sys.exit()
    

def connect_socket():
    global host
    global port
    global s
    
    try:
        s.bind((host,port))
        s.listen(5)
        print("Connected successfully!!!!!!!!!!!!!")
        
    except socket.error as err:
        print("Could not connect.............")
        

def accept_server():
    global host
    global port
    global s
    global conn

    try:
        conn,addr = s.accept()
        print("Connected to......",str(addr))
    except:
        print("But not accepted")

def send_message():
    global host
    global port
    global s
    global conn

    
    msg = input("Enter here to send anything:  ") 
    if msg == "exit":
        sys.exit()

    conn.send(str.encode(msg,"utf-8"))


def receive_message():
    global host
    global port
    global s
    global conn

    data = conn.recv(1024)
    print("Reply: " + data.decode("utf-8"))


create_socket()
connect_socket()
accept_server()

while True:
    ch = input("Send or receive?(s/r): ")
    if ch == "exit":
        sys.exit()
    elif ch == 's':
        send_message()

    elif ch == 'r':
        print(" ")
        receive_message()

