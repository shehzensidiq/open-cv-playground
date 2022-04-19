import cv2

def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)

image = cv2.imread("example.jpg")
show("default", image)

cv2.destroyAllWindows()