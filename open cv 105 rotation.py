import cv2
import numpy as np

# load the image
file = "cat.jpg"
image = cv2.imread(file)


# function for displaying the images, wont have to write the code again and agian


def show(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

show("original", image)
# make the rotation
# the logic:

''' for rotation we need to decide a pivot point, alonf which the rotation will take
place, it is like deciding a nail on the image and then making the image
rotate along that nail.'''
# we will do the rotation along the centre point,
height, width = image.shape[:2]
centerX, centerY = width // 2, height // 2

# we will create a rotation matrix
# this matrix will contain the conditions for our rotation like
# the point along which the rotation has to be done, the degrees of rotation,
# and the scale for the rotated image.
# - angles means clockeise and + anti clockwise

r_m = cv2.getRotationMatrix2D((centerX, centerY), 23, 1)
# then we need to affineWarp this matrix with the image
anti_rot = cv2.warpAffine(image, r_m, image.shape[:2])
show("rotated", anti_rot)

r_m = cv2.getRotationMatrix2D((centerX, centerY), -23, 1)
# then we need to affineWarp this matrix with the image
clock_rot = cv2.warpAffine(image, r_m, image.shape[:2])
show("col rotated", clock_rot)

# we can write a function to wrap these two line in one
def rotate_image(pivot, image, angle, scale=1):
    rm = cv2.getRotationMatrix2D(pivot, angle, scale)
    rot = cv2.warpAffine(image, rm, image.shape[:2])
    return rot

one = rotate_image((centerX, centerY), image, 45)
show("function rotated", one)

# we can use the imutils to perform this rotation etc, it is using the
# same cv2 code
import imutils as im

im = im.rotate(image, 33, (centerX, centerY))
show("imutils rotation", im)
