# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:07:23 2019

@author: Shaggy
"""

import os      #both
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk,Image

#======================emotion detection===============
import image             
import cv2              # image processing library
import numpy as np    # image feature 
from keras.models import load_model  # dataset
root=Tk()
root.geometry('1000x800')
root.title("Mood Player")
menubar = Menu(root)
root.config(menu=menubar)

logo=PhotoImage(file="logo.png")
Button(root,text='Logo',image=logo,width=20,height=20,bg="#8243BA").place(x=10,y=10)
C = Canvas(root,width=1080,height=1080)
image=ImageTk.PhotoImage(Image.open("back.png"))
C.create_image(0,0,anchor=NW,image=image)
C.pack()
def play_music():
    try:
        paused
    except NameError:
        try:
            # mixer.music.load("song.wav")
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing Music" + " - " + os.path.basename(filename)
        except:
            tkinter.messagebox.showerror('No file is uploaded', 'Mood Player could not find the music')
    else:
        mixer.music.unpause()
        statusbar['text']="Music Resumed"


playphoto= PhotoImage(file='play.png')
pausephoto=PhotoImage(file='pause.png')
logophoto=PhotoImage(file='logo.png')
Button(root,text='submit',image=playphoto,background='#B36CF3',command=play_music,width=62,fg='orange').place(x=20,y=0)
Button(root,text='submit',image=pausephoto,background='#B36CF3',command=play_music,width=62,fg='orange').place(x=80,y=0)
Button(root,text='submit',image=logophoto,command=play_music,width=1200,fg='orange').place(x=80,y=0)
root.mainloop()