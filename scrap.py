from bs4 import BeautifulSoup
import os 
import sys
import requests
import webbrowser

s = f""" 
         ***************
         ***************
         ***************
         ***************
    ************************
     **********************
       ******************
      _____         _____        
    /      \       /     \ 
   |        -------       |
    \ ____ /  ***  \_____/ 
             *****
            *******
           *********
     
   
   ssss   sssss      s      ssss   s     s          sss     ssss   ssss      s     sss   sss  s     s
   s   s  s         s s     s   s   s   s          s       s       s   s    s s    s  s  s  s  s   s
   ssss   sss      s   s    s   s     s             ss    s        ssss    s   s   sss   sss     s
   s s    s       sssssss   s   s     s               s    s       s s    sssssss  s     s       s
   s  s   sssss   s     s   ssss      s            sss      ssss   s  s   s     s  s     s       s
 """

print(s)

print("Hello I am scrappy.......I am here to help you in finding the html codes and finding the link among them.......so get started.......")

print("Enter your url here: ")  #Enter any url you want
url = input()

resp = requests.get(url) #Resonse is collected from url

total_content = list(resp) #The responseobjects are kept n a list

soup = BeautifulSoup(resp.content,'html.parser') #A soup object is created

ch = ""

while(ch != 'link'):
  ch = input("Enter 'link' to find all the links: ")
  if ch != 'link':
    print("Please enter 'link'..not ",ch)

links = []
classes = []

if ch == 'link':
  selc = []
  for tag in soup.find_all('a'):
    t = tag.get('href')
    links.append(t)
  
  if len(links) == 0:
    print("No links...............")
    sys.exit()
  
  print("Links collected")
  # Here, you have to enter ant word or piece of word and the links containing the word will be displayed
  f = input("Enter any link realted word you want or enter 'all' to display all the links collected: ") 
  
  if f == 'all':
    i = 0
    for i in range(len(links)):
      print(links[i])

  else:
    for web in links:
      if f in web:
        print(web)
        selc.append(web)
  
    if len(selc) == 0:
      print("No linkls found accordng to you r search...........")
      sys.exit()
 
  c = input("Do you want to visit any link?(y/n) ")
  if c == 'y':
    lnk = input("Enter the link here: ")
    if lnk in selc or link in links:
      webbrowser.open(lnk)

    else:
      print("Link is not in collection...................")
      sys.exit()

  elif c == 'n':
    sys.exit()                      
