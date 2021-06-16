import os
import subprocess
import pprint
from tkinter import messagebox

#os.system('netsh wlan show profiles')
from subprocess import run
output = run('netsh wlan show profiles', capture_output=True).stdout
#print(output)
ls = str(output)
wifi = ls.split('    All User Profile     ')
#print(wifi)
wifi.remove(wifi[0])
print('All the available Wifi networks are: ')
print('')
for w in wifi:
    print(w[2:(len(w) - 4)])
#[2:(len(wifi[0]) - 4)]
print('')
while(1):
    a = input("Enter the wifi you want to know the password (Enter name in double quotes if they contain spaces or Enter 'exit' to end application): ")
    if a == 'exit':
        break
    cmd = 'netsh wlan show profiles ' + a + ' key=clear'
    out = run(cmd, capture_output=True).stdout
    out_str = str(out)
    out_list = out_str.split("\\r\\n")
    key = "Key Content"
    print('')
    print('')
    for word in out_list:
        if key in word:
            print("The password you are looking for is : " + word[28:len(word)])
            passwd = str(word[28:len(word)])
        
            messagebox.showinfo('Here is the password', passwd)
    
    print('')
    print('')
    