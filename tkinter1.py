from tkinter import *

root = Tk() # always the first window when working with tkinter creates the main window

#always 2 steps create the thing then display it

myLabel = Label(root, text = "Dyenoh ni Mzii") # the label to go into the root widget and the text to display

myLabel.pack() #pack the label into the window (just anywhere)

root.mainloop() #to display the window 