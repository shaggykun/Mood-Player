# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:26:42 2019

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

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

#=====================  here we go  ===============
root = Toplevel()
#MENUBAR
menubar = Menu(root)
root.config(menu=menubar)
root.configure(background='#180CB4')
root.geometry('900x1080')

logo=PhotoImage(file="logo.png")
label=Label(root,image=logo,bg="#8243BA")
label.place(x=0,y=0)

C = Canvas(root,width=900,height=1080)
image=ImageTk.PhotoImage(Image.open("back.png"))
C.create_image(0,0,anchor=NW,image=image)
C.pack()

#==========================browsing file===========
def browse_file():
    global filename
    filename=filedialog.askopenfilename()
    print(filename)

#CREATE Submenu
subMenu= Menu(menubar, tearoff=0 )
menubar.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label="Open",command=browse_file)
subMenu.add_command(label="Exit",command=root.destroy)



#=================================================
def about_us():
    tkinter.messagebox.showinfo('About Mood Player','This is a music player which plays music according to your mood.')
subMenu= Menu(menubar, tearoff=0 )
menubar.add_cascade(label='Help',menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)
subMenu.add_command(label="Tutorials")

#=========automatic playing==============

def auto_play():
    
    video_capture = cv2.VideoCapture(0)      #for camera  of laptop.....
    model = load_model('keras_model/model_5-49-0.62.hdf5')

    target = ['angry','disgust','fear','happy','sad','surprise','neutral']
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        frame=cv2.flip(frame,1,0)  #flip to act as mirror

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1)

    # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2,5)
            face_crop = frame[y:y+h,x:x+w]
            face_crop = cv2.resize(face_crop,(48,48))
            face_crop = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
            face_crop = face_crop.astype('float32')/255
            face_crop = np.asarray(face_crop)
            face_crop = face_crop.reshape(1, 1,face_crop.shape[0],face_crop.shape[1])
            result = target[np.argmax(model.predict(face_crop))]
            cv2.putText(frame,result,(x,y), font, 1, (200,0,0), 3, cv2.LINE_AA)

    # Display the resulting frame
        cv2.imshow('Video', frame)
    

        if cv2.waitKey(10) ==27:
            break

# When everything is done, release the capture
    video_capture.release()
    print('playing song for')
    print(result)
    #========================command for differnt mood==========
    if(result=="happy"):
        hap()
    elif(result=="sad"):
        sad()
    elif(result=="surprise"):
        surprise()
    elif(result=="fear"):
        fear()
    elif(result=="neutral"):
        neutral()
    elif(result=="angry"):
        angry()
    
    #displays the final expression u had bwfore exiting....
    cv2.destroyAllWindows()

#====================== function for emotions ============

def hap():            # song for happy
  
   p='Selfie Maine Leli Aaj  (RaagJatt.com).mp3'
   mixer.init()                               
   mixer.music.load(p) 
   mixer.music.play()
   statusbar['text'] = "Playing Music" + " - " + os.path.basename(p)

def sad():            # song for sad
  
   p='jane_kaha_gaye_wodin.mp3'
   mixer.init()                               
   mixer.music.load(p) 
   mixer.music.play()
   statusbar['text'] = "Playing Music" + " - " + os.path.basename(p)

def fear():            # song for fear
  
   p='deva_shree_ganesha.mp3'
   mixer.init()                               
   mixer.music.load(p) 
   mixer.music.play()
   statusbar['text'] = "Playing Music" + " - " + os.path.basename(p)


def surprise():            # song for surprise
  
   p='uchiyan ne gallan.mp3'
   mixer.init()                               
   mixer.music.load(p) 
   mixer.music.play()
   statusbar['text'] = "Playing Music" + " - " + os.path.basename(p)

                       #song for neutral
def neutral():
    
    p='09 - Sidewalks (feat. Kendrick Lamar).mp3'
    mixer.init()                               
    mixer.music.load(p) 
    mixer.music.play()
    statusbar['text'] = "Playing Music" + " - " + os.path.basename(p)
    
def angry():
    
    p='angry.mp3'
    mixer.init()                               
    mixer.music.load(p) 
    mixer.music.play()
    statusbar['text'] = "Playing Music" + " - " + os.path.basename(p)
    

mixer.init()    #initializing the mixer


root.title("Mood Player")
#root.iconbitmap(r'mood.ico')

text=Label(root,text='Play your Mood!')
text.pack(pady=10)



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


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"

def pause_music():
    global paused
    paused= TRUE
    mixer.music.pause()
    statusbar['text']="Music Paused"

def set_vol(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)

muted = FALSE

def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE
        
middleframe=Frame(root,bg='#8243BA')
middleframe.pack(padx=10,pady=10)

playphoto= PhotoImage(file='play.png')
playBtn=Button(middleframe, image=playphoto, command=play_music)
playBtn.configure(background='#B36CF3')
playBtn.place(x=100,y=200)

stopphoto= PhotoImage(file='stop.png')
stopBtn=Button(middleframe, image=stopphoto, command=stop_music)
stopBtn.configure(background='#B36CF3')
stopBtn.place(x=200,y=200)

pausephoto= PhotoImage(file='pause.png')
pauseBtn=Button(middleframe, image=pausephoto, command=pause_music)
pauseBtn.configure(background='#B36CF3')
pauseBtn.place(x=300,y=200)

openPhoto= PhotoImage(file='openn.png')
openBtn= Button(root,image=openPhoto ,command= browse_file)
openBtn.place(x=400,y=500)

scale= Scale(root, from_=0,to =100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(70)
scale.place(relx=0.2,rely=0.5)
scale.configure(background='#8243BA')
scale.place(x=200,y=400)

mutePhoto = PhotoImage(file='mute.png')
volumePhoto = PhotoImage(file='volume.png')
volumeBtn = Button(root, image=volumePhoto, command= mute_music)
volumeBtn.configure(background='#8243BA')
volumeBtn.place(x=200,y=500)


aboutPhoto= PhotoImage(file='load.png')
aboutBtn=Button(root,image=aboutPhoto, command=auto_play)
aboutBtn.configure(background='#8243BA')
aboutBtn.place(x=500,y=700)


statusbar=Label(root,text="Welcome to Mood Player",relief=SUNKEN,anchor=SW)
statusbar.config(width=200)
statusbar.configure(background='#8243BA')
statusbar.place(x=0,y=0)

root.mainloop()
