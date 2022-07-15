from tkinter import *

root = Tk() # always the first window when working with tkinter creates the main window

#always 2 steps create the thing then display it

myLabel1 = Label(root, text = "Dyenoh ni Mzii") # the label to go into the root widget and the text to display
myLabel2 = Label(root, text = "Tena sana")

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)


root.mainloop() #to display the window 

 #KSDJFH