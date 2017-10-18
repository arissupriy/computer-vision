import cv2
import os
from matplotlib import pyplot as plt

# for get url/directory name
base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_url = os.path.join(base_url, '00_image')

# image name
image = os.path.join(image_url, 'aircraft.jpg')
b,g,r = cv2.split(cv2.imread(image))

# image read with GRAYSCALE_PARAMS
gray_image = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)

# Convert grayscale image to binary | Thresholding | otsu
thresh = 128
im_bw = cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)[1]

# Or u can use it for auto threshold with otsu
# (thresh, im_bw) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

plt.subplot(3,1,1),  plt.imshow(cv2.merge((r,g,b)), cmap=None)
plt.title('Original Noisy Image'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2), plt.hist(gray_image.ravel(), 256)
plt.axvline(x=thresh, color='r')
plt.title('Histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(im_bw, cmap='gray')
plt.title('Black White'), plt.xticks([]), plt.yticks([])
plt.show()


