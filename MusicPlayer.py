import os
import pygame
from tkinter import *
import tkinter.filedialog

root = Tk()
root.minsize(300,300)

songList = []
index = 0


def pickDirectory():
	directory = os.getcwd()
		
	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			songList.append(files)


	pygame.mixer.init()
	pygame.mixer.music.load(songList[index])
	pygame.mixer.music.play()

pickDirectory()
	
label = Label(root, text = "Audio Player")
label.pack()	
listbox = Listbox(root)
listbox.pack()

songList.reverse()

for items in songList:
	listbox.insert(0, items)

songList.reverse()

nextButton = Button(root, text = "Next")
nextButton.pack()

previousButton = Button(root, text = "Previous")
previousButton.pack()

stopButton = Button(root, text = "Stop")
stopButton.pack()
	

	
root.mainloop()
