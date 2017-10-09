import cv2
from matplotlib import pyplot as plt

image_url = '../01-image/aircraft.jpg'

image = cv2.imread('aircraft.jpg')

plt.hist(image.ravel(),256,[0,256])
plt.show()

