import cv2
import os

# for get url/directory name
base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_url = os.path.join(base_url, '00_image')

# image name
image = os.path.join(image_url, 'aircraft.jpg')

#image read with GRAYSCALE_PARAMS
image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)


cv2.imshow('Label', image)
cv2.waitKey()

