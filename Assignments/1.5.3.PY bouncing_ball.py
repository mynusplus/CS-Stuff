#####
# bouncing_ball.py
# 
# Creates a Scale and a Canvas. Animates a circle based on the Scale
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
speed_intvar = tkinter.IntVar()
speed_intvar.set(1) # Initialize y coordinate
# radius and x-coordinate of circle
r = 10
x = 150
y = 150
direction = 0.5 # radians of angle in standard position, ccw from positive x axis
 
######
# Create Controller
#######
# Instantiate and place slider
speed_slider = tkinter.Scale(root, from_=3, to=1, variable=speed_intvar,    
                              label='speed')
speed_slider.grid(row=1, column=0, sticky=tkinter.W)
# Create and place directions for the user
text = tkinter.Label(root, text='Drag slider \nto adjust\nspeed.')
text.grid(row=0, column =0)

######
# Create View
#######
# Create and place a canvas
canvas = tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
import math
def animate():
    # Get the slider data and create x- and y-components of velocity
    velocity_x = speed_intvar.get() * math.cos(direction) / 3 # adj = hyp*cos()
    velocity_y = speed_intvar.get() * math.sin(direction) / 3 # opp = hyp*sin()
    # Change the canvas item's coordinates
    canvas.move(circle_item, velocity_x, velocity_y)
    
    # Get the new coordinates and act accordingly if ball is at an edge
    x1, y1, x2, y2 = canvas.coords(circle_item)
    global direction
    # If crossing left or right of canvas
    if x2>canvas.winfo_width(): 
        canvas.move(circle_item, -canvas.winfo_width(), 0)
    if x1<0:
        canvas.move(circle_item, canvas.winfo_width(), 0)
    # If crossing top or bottom of canvas
    if y2>canvas.winfo_height() or y1<0: 
        direction = -1 * direction # Reverse the y-component of velocity
    
    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion        
    canvas.after(1, animate)
# Call function directly to start the recursion
animate()

#######
# Event Loop
#######
root.mainloop()