#####
# color_string_changer.py
# 
# Creates two Scales and a Text view. Updates Text based on the Scales
# 
# (c) 2013 PLTW
# version 11/1/2013
####

import tkinter # Often people import Tkinter as *

#####
# Create root window 
####
root = tkinter.Tk()
root.wm_title('Hexadecimal Explorer')

#####
# Create Model
######
# Create two IntVar's and initialize them to 127
red_intvar = tkinter.IntVar() 
red_intvar.set(127) 
green_intvar = tkinter.IntVar()
green_intvar.set(127)
# center of circle
x = 150 
y = 150
#radius of circle
r = 100

######
# Create Controller
#######
# Event handler for slider
def color_changed(new_intval):
    # Controller updates the view by pulling data from model
    h = '#' + \
        hexstring(red_intvar) + \
        hexstring(green_intvar) + '00\n'
    editor.insert(tkinter.END, h)
    editor.see(tkinter.END) # scroll the Text window to see the new bottom line
    canvas.itemconfig(circle_item, fill=h)
# Instantiate and place sliders
red_slider = tkinter.Scale(root, from_=0, to=255, variable=red_intvar, 
                           orient=tkinter.HORIZONTAL,   
                           label='Red', command=color_changed)
red_slider.grid(row=1, column=0, sticky=tkinter.E)
green_slider = tkinter.Scale(root, from_=0, to=255, variable=green_intvar,  
                             orient=tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=2, column=0, sticky=tkinter.E)
# Create and place directions for the user
text = tkinter.Label(root, text='Drag slider \nto adjust\ncolor code.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create a text editor window for displaying information
editor = tkinter.Text(root, width=10)
editor.grid(column=2, row=0, rowspan=3)
# Create and place a canvas
canvas = tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')

######
# Function to convert IntVar data from Scale widget to two hex digits as string
# for a Canvas widget color argument
#######

def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a 2-character string representing a value in hexadecimal
    '''
    # Get an integer from an IntVar
    slider_int = slider_intvar.get()
    # Convert to hex
    slider_hex = hex(slider_int)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits

#######
# Event Loop
#######
root.mainloop()