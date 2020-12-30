import requests
from time import time, sleep
from tqdm import tqdm  
import tkinter
from tkinter import PhotoImage
import os
from tkinter import Text, filedialog, simpledialog
import PIL
from PIL import ImageTk, Image

# This is the downloader section 

def download():
    URL = entry.get()
    chunk_size = 4096000
    url = URL
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    MB = total_size/  1000000
    print('Total size of content: ' + str(total_size) + 'Bits')
    with open('F:\\aaa_python.mp4', 'wb') as file:
        for c in r.iter_content(chunk_size=chunk_size):
            progress_bar.update(len(c))
            file.write(c)
            progress_bar.close()
            
    if total_size != 0 and progress_bar.n != total_size:
        print('Something Error occured!!!!')
        print(progress_bar.n)
    
    else:
        print('File downloaded')


# This is the UI section


root = tkinter.Tk()

canvas = tkinter.Canvas(root, height=350, width=700, bg='green')
canvas.pack()
canvas.create_text(350,100,fill="darkblue",font="Times 20 italic bold",
                     text="Video/Image Downloader")
canvas.create_text(350, 50, fill="darkblue", font="Times 20", text="Enter exact photo/video url to download it")

frame = tkinter.Frame(root, bg='yellow')
frame.place(relwidth=0.5, relheight=0.05, relx=0.25, rely=0.35)

button = tkinter.Button(root, text="Download", fg="black", bg="yellow", command=download)
button.pack(padx=5, pady=20)

entry = tkinter.Entry(frame, text="URL", relief="sunken", width=60)
entry.pack()

root.mainloop()

'''https://cdn.lynda.com/static/nonmember/images/client-logos/nbc.png'''