import os
import pygame
from tkinter import *
from mutagen.id3 import ID3

root = Tk()
root.minsize(300,300)

songList = []
nameMetaData = []

songname = ""
v = StringVar()
songLabel = Label(root, textvariable = v, width = 35)

index = 0

def nextSong(event):
	global index
	if index < len(songList) - 1:
		index += 1
		pygame.mixer.music.load(songList[index])
		pygame.mixer.music.play()
		updateNameLabel()

def previousSong(event):
	global index
	if index > 0:
		index -= 1
		pygame.mixer.music.load(songList[index])
		pygame.mixer.music.play()
		updateNameLabel()

def stopSong(event):
	pygame.mixer.music.stop()
	v.set("")
	return songname

def updateNameLabel():
	global index
	global songname
	v.set(nameMetaData[index])
	return songname

def pickDirectory():
	directory = os.getcwd()
		
	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			dir = os.path.realpath(files)
			song = ID3(dir)
			nameMetaData.append(song['TIT2'].text[0])
			songList.append(files)


	pygame.mixer.init()
	pygame.mixer.music.load(songList[index])
	pygame.mixer.music.play()
	updateNameLabel()

pickDirectory()
	
label = Label(root, text = "Audio Player")
label.pack()	
listbox = Listbox(root)
listbox.pack()

for items in nameMetaData:
	listbox.insert(END, items)


nextButton = Button(root, text = "Next")
nextButton.pack()

previousButton = Button(root, text = "Previous")
previousButton.pack()

stopButton = Button(root, text = "Stop")
stopButton.pack()
	
nextButton.bind("<Button-1>", nextSong)
previousButton.bind("<Button-1>", previousSong)
stopButton.bind("<Button-1>", stopSong)

songLabel.pack()

root.mainloop()
