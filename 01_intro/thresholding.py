import cv2
import os

# for get url/directory name
base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_url = os.path.join(base_url, '00_image')

# image name
image = os.path.join(image_url, 'aircraft.jpg')

# image read with GRAYSCALE_PARAMS
image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)

# Convert grayscale image to binary
(thresh, img) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print thresh
print img

