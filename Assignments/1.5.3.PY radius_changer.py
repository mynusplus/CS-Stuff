#####
# height_changer.py
# 
# Creates a Scale and a Canvas. Updates a circle based on the Scale.
# (c) 2013 PLTW
# version 11/1/2013
####

import tkinter #often people import Tkinter as *

#####
# Create root window 
####
root = tkinter.Tk()

#####
# Create Model
######
height_intvar = tkinter.IntVar()
height_intvar.set(0) #initialize height
# center of circle
x = 150 
y = 150
#radius of circle
r = 100

######
# Create Controller
#######
# Event handler for slider
def height_changed(new_intval):
    # Get data from model
    # Could do this: h = int(new_intval)
    h = height_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-r, y+h-r, x+r, y+h+r)
# Instantiate and place slider
height_slider = tkinter.Scale(root, from_=-100, to=100, variable=height_intvar,    
                              label='Height', command=height_changed)
height_slider.grid(row=1, column=0, sticky=tkinter.W)
# Create and place directions for the user
text = tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create and place a canvas
canvas = tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
#######
# Event Loop
#######
root.mainloop()