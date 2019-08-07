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

ch = input("Enter 'link' to find all the links.......'id' to find all id's.................")

links = []
classes = []

if ch == 'link':
  selc = []
  for tag in soup.find_all('a'):
    t = tag.get('href')
    links.append(t)
  
  print("Links collected")
  # Here, you have to enter ant word or piece of word and the links containing the word will be displayed
  f = input("Enter any link realted word you want: ") 
  
  for web in links:
    if f in web:
      print(web)
      selc.append(web)

  c = input("Do you want to visit any link?(y/n) ")
  if c == 'y':
    lnk = input("Enter the link here: ")
    if lnk in selc:
      webbrowser.open(lnk)

    else:
      print("Link is not in list...................")
      sys.exit()

  elif c == 'n':
    sys.exit()                      