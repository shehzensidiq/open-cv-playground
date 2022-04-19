import cv2
import numpy as np
# Photo by Kirsten Bühne: https://www.pexels.com/photo/selective-focus-photo-of-grey-cat-1521304/
# load the image
image_path = "cat.jpg"
image = cv2.imread(image_path)

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# create a translation matrix
# a translation matrix is a matrix of same shape of the input image.
# [0, 1, shiftY] = > [xof, yon, yShift]
# [1,0, shiftY] => [xon, yof, xShift]
# this matrix should be float and then we need to do the affinewarp.
# this will shift the image 24 towards right and 34 down. Thus + x makes the image move
# right and + y makes the image go down
shift_x, shift_y = [1, 0, 24], [0, 1, 34]
translation_m = np.float32([shift_x, shift_y])
i = cv2.warpAffine(image, translation_m, image.shape[:2])
cv2.imshow("Translated with 24 x and 34 y", i)
cv2.waitKey(0)
# cv2.destroyAllWindows()
# apply the translation
# The -x will make the image go left and -y will make the image move up.

shift_x, shift_y = [1, 0, -24], [0, 1, -34]
translation_m = np.float32([shift_x, shift_y])
i = cv2.warpAffine(image, translation_m, image.shape[:2])
cv2.imshow("Translated with -24 x and -34 y", i)
cv2.waitKey(0)
cv2.destroyAllWindows()

# shifting along the one axis
shift_x, shift_y = [1, 0, 45], [0, 1, 0]
translation_m = np.float32([shift_x, shift_y])
i = cv2.warpAffine(image, translation_m, image.shape[:2])
cv2.imshow("Translated with 45 x", i)
cv2.waitKey(0)
cv2.destroyAllWindows()
# using imutils, which uses the same functions but wraps
# them in simple to use functions
import imutils as im

t = im.translate(image, 0, 160)
cv2.imshow("Translated with imutils", t)
cv2.waitKey(0)
cv2.destroyAllWindows()