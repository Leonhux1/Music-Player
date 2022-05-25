import tkinter

from tkinter import *

import tkinter.messagebox

from tkinter import messagebox

from PIL import ImageTk, Image

from tkinter import filedialog

import os

import pygame

from pygame import mixer

from tkinter import font

import random

global times

global state

global main

global musicBox

global playButton

global scale

global songslist

global mainDict

global control

global checkGetter

mainDict = {}

songslist = []

state = ''

times = 1

control = "backshift"

checkGetter = ''

listPlay = []

myset = set()

myset2 = set()

listPlay2 = []

getter2 = ''
# Information for key hovers.
def information():
    tkinter.messagebox.showinfo("Instructions", "Welcome! Sir/Madam, this Music Player allows you to select Mp3 music from any where in your computer by clicking the file button on" +
                                " the top left corner of the interface. You can then select any music from the box in the center" +
                                " of the program and play it using the pause/play button. Note that you cant load music from two directories at the same time." +
                                " You can also set the volume to your preference and can stop the playback of the music any time you like. You can also navigate through songs using the forward and backward buttons" +
                                " at right and left of your pause/play button repectively. Have fun!")
                                
def play_Hover(req):
    statusBar.config(text = "Play")

def play_Hover_Quit(req):
    statusBar.config(text = "")

def exit_Hover(req1):
    statusBar.config(text = "Quit")

def exit_Hover_Quit(req1):
    statusBar.config(text = "")

def stop_Hover(req2):
    statusBar.config(text = "Stop Playback")

def stop_Hover_Quit(req2):
    statusBar.config(text = "")

def back_Hover(req3):
    statusBar.config(text = "Previous Song")

def back_Hover_Quit(req3):
    statusBar.config(text = "")

def forward_Hover(req4):
    statusBar.config(text = "Next Song")

def forward_Hover_Quit(req4):
    statusBar.config(text = "")

def folder_Hover(req5):
    statusBar.config(text = "Import Music to play!")

def folder_Hover_Quit(req5):
    statusBar.config(text = "")

def info_Hover(req6):
    statusBar.config(text = "Information about the Music Player")

def info_Hover_Quit(req6):
    statusBar.config(text = "")

def scale_Hover(req7):
    statusBar.config(text = "Adjust the Volume")

def scale_Hover_Quit(req7):
    statusBar.config(text = "")

# Defining the functions for the buttons.
def directories():
    try: 
        musicBox.delete(0, 'end')
        
        files = filedialog.askdirectory(initialdir = "C:", title = "Select a File")

        path = os.listdir(files)
        
        for element in range(len(path)):
            name = str(path[element])
            if name.endswith(".wav") or name.endswith(".mp3"):
                full_File_Name = os.path.join(files, name)
                songslist.append(full_File_Name)

        for element in songslist:
            mainDict[os.path.basename(element)] = element
            

        print(mainDict)
        for songs in mainDict.keys():
            musicBox.insert(END, songs)
    except(FileNotFoundError):
        tkinter.messagebox.showinfo("Music Box", "No file found for playing.")


    
def partyTime():
    try:
        global times

        global state

        global checkGetter
        
        state2 = ""

        getter = musicBox.get(ACTIVE)

        myset.add(getter)

        if len(myset) == 2:
            listPlay = list(myset)
            getter = listPlay[1]
            listPlay.clear()
            myset.clear()
            times = 1
            playButton.config(image = playPic)
            scale.set(0)
            
        if state == "stopped":
            mixer.music.load(mainDict[musicBox.get(ACTIVE)])
            mixer.music.play(loops = -1)
            state2 = "play2"
        
        if times % 2 != 0:
            state = 'play'
            
        else:
            state = 'paused'
            times += 1

        if state == 'play' and times == 1:

            pygame.mixer.music.load(mainDict[musicBox.get(ACTIVE)])

            pygame.mixer.music.play(-1)

            playButton.config(image = pausePic)

            mixer.music.set_volume(0)

            times += 1

        elif state == 'play':
            pygame.mixer.music.unpause()
            playButton.config(image = pausePic)
            times += 1

        elif(state == 'paused'):
            playButton.config(image = playPic)
            pygame.mixer.music.pause()

    except(KeyError):
        tkinter.messagebox.showinfo("Music Box", "No item in music box to be played.")

def quitting():
    if messagebox.askokcancel("Quit", "Do you want to quit"):
        pygame.mixer.quit()
        main.destroy()

def volume(var):
    pygame.mixer.music.set_volume(scale.get() / 100)

def whyClose():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        pygame.mixer.quit()
        main.destroy()

# Stop button has a little problem.    
def halter():
    global state
    global times
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    musicBox.selection_clear(ACTIVE)
    playButton.config(image = playPic)
    times = 1
    scale.set(0)
    

def forward():
    global control
    global times

    try:
        nowIs = musicBox.curselection()
        nowIs = nowIs[0] + 1

        
        currentlyPlaying = ''
        currentlyPlaying = musicBox.get(nowIs)

        pygame.mixer.music.load(mainDict[currentlyPlaying])
        pygame.mixer.music.play(loops = -1)
        playButton.config(image = pausePic)

        musicBox.selection_clear(0, 'end')

        musicBox.activate(nowIs)

        musicBox.selection_set(nowIs, last = None)

        testing = musicBox.curselection()
        if(testing[0] == musicBox.size() - 1):
            control = "shift"
            
        if(pygame.mixer.music.get_busy()):
            playButton.config(image = pausePic)
            
        else:
            playButton.config(image = playPic)

    except(KeyError):
        tkinter.messagebox.showinfo("Forward Button", "Last sound reached, cannot go beyond this. Please scroll upwards.")
    except(IndexError):
        tkinter.messagebox.showinfo("Forward Button", "No sound to move forward to.")

def backward():
    try:
        nowIs1 = musicBox.curselection()
        nowIs1 = nowIs1[0] - 1

        currentlyPlaying1 = ''
        
        currentlyPlaying1 = musicBox.get(nowIs1)

        pygame.mixer.music.load(mainDict[currentlyPlaying1])
        pygame.mixer.music.play(loops = 0)

        musicBox.selection_clear(0, 'end')

        musicBox.activate(nowIs1)

        musicBox.selection_set(nowIs1, last = None)

        if(pygame.mixer.music.get_busy):
            playButton.config(image = pausePic)
        else:
            playButton.config(image = playPic)
            
    except(KeyError):
        tkinter.messagebox.showinfo("Backward Button", "Last sound reached, cannot go beyond this. Please scroll downwards.")
    except(IndexError):
        tkinter.messagebox.showinfo("Backward Button", "No sound to move back to.")
        


# Interface design begins here.
color = "slategrey"

pygame.mixer.init()

main = tkinter.Tk()

main.resizable(False, False)

main.protocol('WM_DELETE_WINDOW', whyClose)

infoPic = PhotoImage(file = "info-button.png")

playPic = PhotoImage(file = "play-button.png")

forwardPic = PhotoImage(file = "forward-button.png")

backPic = PhotoImage(file = "previous-button.png")

pausePic = PhotoImage(file = "pause-button.png")

stopPic = PhotoImage(file = "stop-button.png")

exitPic = PhotoImage(file = "exit-button.png")

folderPic = PhotoImage(file = "folder-button.png")

main.title("Faizan Rafieuddin's Music Player")

main.geometry("460x560")

main.configure(background = "slategrey")

firstFrame = tkinter.Frame(main, width = 460, height = 100, bg = "slategrey")

firstFrame.pack()

exitButton = tkinter.Button(firstFrame, image = exitPic, compound = LEFT, bg = "slategrey", bd = 0, activebackground = "slategrey",anchor = E, command = quitting)

exitButton.pack(side = RIGHT, ipadx = 97)

exitButton.bind("<Enter>", exit_Hover)

exitButton.bind("<Leave>", exit_Hover_Quit)

folderButton = tkinter.Button(firstFrame, image = folderPic, compound = LEFT, bg = "slategrey", bd = 0, activebackground = "slategrey", anchor = W, command = directories)

folderButton.pack(side = LEFT, ipadx = 97)

folderButton.bind("<Enter>", folder_Hover)

folderButton.bind("<Leave>", folder_Hover_Quit)

buttonFrame = tkinter.Frame(main, width = 460, height = 150, bg = "slategrey", bd = 0)

buttonFrame.pack(side = BOTTOM)

stopButton = tkinter.Button(buttonFrame, image = stopPic, compound = LEFT, bg = "slategrey", bd = 0, activebackground = "slategrey", command = halter)

stopButton.pack(side = LEFT , padx = 10)

stopButton.bind("<Enter>", stop_Hover)

stopButton.bind("<Leave>", stop_Hover_Quit)

scale = tkinter.Scale(main, from_ = 100, to = 0, sliderlength = 20, bg = "slategrey", bd = 0, width = 15, highlightthickness = 0, activebackground = "slategrey", highlightcolor = "slategrey", relief = RAISED, command = volume)

scale.pack(side = LEFT)

musicBox = tkinter.Listbox(main, width = 50, bg = "steelblue", height = 17, bd = 1, relief = RAISED, selectbackground = 'Blue', selectforeground = 'white')

musicBox.place(x = 82, y = 50)

scale.bind("<Enter>", scale_Hover)

scale.bind("<Leave>", scale_Hover_Quit)

backButton = tkinter.Button(buttonFrame, image = backPic, compound = LEFT, bg = "slategrey", bd = 0, activebackground = "slategrey", command = backward)

backButton.pack(side = LEFT, padx = 10)

backButton.bind("<Enter>", back_Hover)

backButton.bind("<Leave>", back_Hover_Quit)

playButton = tkinter.Button(buttonFrame, image = playPic, compound = LEFT, bg = "slategrey", bd = 0, activebackground = "slategrey", command = partyTime)

playButton.pack(side = LEFT)

playButton.bind("<Enter>", play_Hover)

playButton.bind("<Leave>", play_Hover_Quit)

forwardButton = tkinter.Button(buttonFrame, image = forwardPic, compound = LEFT, bg = "slategrey", bd = 0, activebackground = "slategrey", command = forward)

forwardButton.pack(side = LEFT, padx = 10)

forwardButton.bind("<Enter>", forward_Hover)

forwardButton.bind("<Leave>", forward_Hover_Quit)

infoButton = tkinter.Button(buttonFrame, image = infoPic, compound = LEFT, bg = "slategrey", bd = 0, activebackground = "slategrey", command = information)

infoButton.pack(side = RIGHT, padx = 10)

infoButton.bind("<Enter>", info_Hover)

infoButton.bind("<Leave>", info_Hover_Quit)

statusBar = tkinter.Label(main, bd = 0, relief = SUNKEN, anchor = E, bg = "slategrey")

statusBar.pack(fill = X, side = BOTTOM, ipady = 2)

main.mainloop()





