import cv2

def show(image, name):
    cv2.imshow("Image show", image)
    cv2.waitKey(0)
#TODO understand the pixels, learn to access the individual pixels
file = "example.jpg"
image = cv2.imread(file)
print(image.shape)
show(image, name="original")

'''Basically, we are getting the first two elements of the tuple, that is containing the shape
of the image along with the color channel. The shape of images has a format of (rows, columns, channels)
it is like 2D matrix of pixels with rows being the height and the columns being the width.'''

height, width = image.shape[:2]
print(f"The height of the image is: {height} and the width is: {width}")

'''We can get the individual pixel values of the pexels simply using the indexing of accesing the
2D array. To get the first pixel of the image that is top left, we index as follows: image[0,0] is
equal to saying image[0][0]. These are same and will return the pixel at 0,0.'''

print(f"The pixel value at image[0,0] is: {image[0,0]}")

'''So we get a tuple with 3 values, these are the values of three colors that make up that pixel. (x,y,z) if, then x
is the intensity of color Blue, y is for green and z is for red. Keep in mind, the open cv follows the BGR color scheme
 not the RGB color scheme. So the returned tuple contains the individual color intensities for BGR.'''
'''If we can get the pixel values, we can also change the pixel intensities. The thing here is that, it is like
changing the value of an array at a particular index. 
`image[row, col]` gives you the particular box in the matrix of pixels, and set it to a tuple
because, we have to provide the value for all three colors.
`image[row, col] = (B,G,R)`

A small point to consider here:
(0,0,255) -> red. we can read this tuple as, 0 intensity for B, 0 for G and 255 for R.
(0,255,0) - Green and (255,0,0) is Blue. the combinations of various intensities of these three colors between 0-255
gives us all the colors that we need. That is the reason Blue , Red and Green are known as Primary colors.  
'''
#TODO change the pixel values
image[0,0] = (255,0,0)
'''After this assignment, now if we check the value of the pixels at the image[0,0], we should get the tuple, we assigned 
to image[0,0]'''

print(f"The tuple after change: {image[0,0]}")
'''`The tuple after change: [255   0   0]`'''
#TODO Assigning the same value - idea of masking - same values
'''we can choose a range of pixels of subsection of an image using split'''
image[0:150, 0:150] = (255,0,0) ## this portion will become blue of the image
cv2.imshow("changed image",image)
cv2.waitKey(0)
image[150:250, 150:250] = (255,155,0) ## this portion will become blue of the image
cv2.imshow("changed image",image)
cv2.waitKey(0)
#TODO crop the images by selecting the range of pixels
'''In the same split fashion, we can crop an image using this split method.'''
# 640 = height, 427 is width
center_row, center_col = 640//2, 427//2
# print(centerX, centerY)
upper_left = image[0:center_row, 0:center_col]
lower_right = image[center_row:, center_col:]
lower_left = image[center_row:, :center_col]
show(upper_left, name="upper_left")
show(lower_right, name="lower right")
show(lower_left, name="lower left")
#TODO: cv follows bgr not the rgb values

'''This is how we play with pixel values in an image.'''