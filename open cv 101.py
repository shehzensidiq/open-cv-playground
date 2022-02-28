#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:00:12 2022

@author: macbookair
"""
""" let us import the open cv and let us see how can we use this pacakage to load and
 display images, then we will use the terminal to pass in the images to the file
 make them processed and also we will see how can we convert one image format to another
 like from png to jpg """
import cv2

'''let us first see how can we load the image, by giving the image itself to the 
function that is going to read the image.'''

'''We have `cv2.imread()`for the purpose of reading an image direct from the file path.'''

image_path = "example.jpg"


'''Let us now load the image'''
im = cv2.imread("example.jpg")
print(im)
'''If you r getting an error of none type, make sure that the path of the image is valid
in spyder, make sure to to change the directory in the upper right corner of the spyder
window to the working drectory, else you will get the error'''

# now let us see the shape of the image,
print(im.shape)

#decoding the shape
print(f"The height: {im.shape[0]} => number of rows")
print(f"The Width: {im.shape[1]} => number of cols")
print(f"The channels: {im.shape[2]} => number of colors")

# let us see the loaded image in a frame
cv2.imshow("Loaded image",im)
cv2.waitKey(0)
'''So we can see, the image displayed in another window.'''

'''Now, let us see how can we save the image and also how easy it is to change the image from 
one extension to another'''
'''So, we have, an image array, with some shape, now let us save the image'''

#cv2.imwrite("new_image.png", im)

# for reading the image from the terminal, we make following changes
import argparse
# initialize the argument parser
parser = argparse.ArgumentParser()
# add the required arguments that need to be passed to the file while run time
parser.add_argument("--name", '-i', required=True, help="Path to image: ")
# create a variable that would contain the parsed args

args = vars(parser.parse_args())
print(args)
'''Thus the args contains the dictionary with the keys as arg names and the values
as the value of the keys'''

# for opening the image we need to pass the agr that contains the path of the image

im = cv2.imread(args["name"])










