# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename1 = os.path.join(directory, 'cat1-a.gif')
filename2 = os.path.join(directory, 'woman.jpg')
filename3 = os.path.join(directory, 'tinyCat.jpg')
# Read the image data into an array
img1 = plt.imread(filename1)
img2 = plt.imread(filename2)
img = plt.imread(filename2)
height = len(img)
width = len(img[0])
for r in range(410, 470):
    for c in range(120, 170):
        if sum(img[r][c])>350 and img[r][c][0] < 200: 
            img[r][c]=[0,0,255] 
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500:
           img[r][c]=[255,0,255] 

'''Show the image data'''
# Number of subplots and which images to put in them
SUBPLOT_NUM = 1
IMAGES_TO_USE = [img2]*SUBPLOT_NUM
# Create a 1xSUBPLOT_NUM grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[i] are the AxesSubplots
fig, ax = plt.subplots(1, SUBPLOT_NUM)
# Show the image data in the selected subplots
ax.imshow(img, interpolation='none')
ax.plot(226,330,'ro')
ax.plot(380,343,'ro')

# Show the figure on the screen
fig.show()


