import cv2
import numpy as np
# load image and display the original
image = cv2.imread("cat.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

# resize without considering the aspect ratio
new_dimension = (300, 150)
resized = cv2.resize(image, new_dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
'''This is the problem with not maintaining aspect ratio'''
# now the question is How do we maintain the aspect ratio of images. Ratio
# simply is the ratio between height and width. For maintaining the aspect ration
# of the image, we take the ratio of new width or height to that of old width or height
# , let us find that
new_width = 100
ratio = 300.0 / image.shape[1]  # width
new_dimension = (300, int(image.shape[0] * ratio))
resized = cv2.resize(image, new_dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("resized 2", resized)
cv2.waitKey(0)
# resizing with the concept of aspect ratio
new_height = 100
ratio = 300.0 / image.shape[0]  # based on height
new_dimension = (int(image.shape[0] * ratio), 300)
resized = cv2.resize(image, new_dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("resized 3", resized)
cv2.waitKey(0)

#imutils
# import imutils as im

# r = im.resize(image, height=or width=)

various_inter = {
    "inter_nearest": cv2.INTER_NEAREST,
    "inter_linear": cv2.INTER_LINEAR,
    "inter_area": cv2.INTER_AREA,
    "inter_cubic": cv2.INTER_CUBIC,
    "inter_lancz": cv2.INTER_LANCZOS4
}