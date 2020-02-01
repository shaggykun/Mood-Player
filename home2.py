import os      #both
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk,Image

root = Tk()

#MENUBAR
menubar = Menu(root)
root.config(menu=menubar)
root.configure(background='#180CB4')
root.geometry('900x1080')

C = Canvas(root,width=900,height=1080)
image=ImageTk.PhotoImage(Image.open("back.png"))
C.create_image(0,0,anchor=NW,image=image)
C.pack()
      
root.mainloop()