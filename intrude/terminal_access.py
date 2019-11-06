import os
import sys
import socket
import subprocess

host = "192.168.56.1"
port = 6666

def server_create():
    global host
    global port
    global s
    
    
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    except socket.error:
        print("Cannot create")
        
def srever_connect():
    global host
    global port
    global s
    
    try:
        s.bind((host,port))
        s.listen(5)
        print("Connected successfully")
        
    except socket.error:
        print("Cannot connect")
        
def srever_accept():
    global host
    global port
    global s
    global conn 
    
    try:
        conn,addr = s.accept()
        print("Accepted...................")
        
    except socket.error:
        print("Cannt accept........")
        
def send_message(msg):
    global host
    global port
    global s
    global conn

    
    #msg = input("Enter here to send anything:  ") 
    if msg == "exit":
        sys.exit()

    conn.send(str.encode(msg,"utf-8"))


def main_task():
    global host
    global port
    global s
    global conn
    
   # cmnd = input("Write command here: ")
   # send_message(cmnd)
    a = conn.recv(200000)
    print(a.decode("utf-8"))
    
            
server_create()
srever_connect()
srever_accept()


while True:
    main_task()
