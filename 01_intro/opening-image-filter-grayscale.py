import cv2

image_url = '../01-image/aircraft.jpg'

image = cv2.imread('aircraft.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Label', image)
cv2.waitKey()

