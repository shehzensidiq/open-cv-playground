import cv2

file = "alphabets.jpeg"


def show(image, window_name):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


#

image = cv2.imread(file)
show(image, "original")
# the 1 for horrizontal flipping or along y axis i.e right to left or vice versa
fliped = cv2.flip(image, 1)

show(fliped, "flipped ")

# 0 will flip the image along the x axis . i.e upside down
fliped_ver = cv2.flip(image, 0)
show(fliped_ver, "flipped vertical")

# for making both axis flip, we pass -1
fliped_both = cv2.flip(image, -1)
show(fliped_both, "flipped both")
