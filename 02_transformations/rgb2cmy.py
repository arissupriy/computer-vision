import cv2
import os
from matplotlib import pyplot as plt

# for get url/directory name
base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_url = os.path.join(base_url, '00_image')

# image name
image = os.path.join(image_url, 'aircraft.jpg')
image = cv2.imread(image)

(b,g,r) = cv2.split(image)

cmy = cv2.merge((1-r,1-g,1-b))

plt.subplot(3,2,1), plt.imshow(cv2.merge((r,g,b)), cmap=None)
plt.title('Ini gambar asli'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,2), plt.hist(cv2.merge((r,g,b)).ravel(), 256)
plt.axvline(x=0, color='r')
plt.title('Histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,3), plt.imshow(cmy)
plt.title('CMYK'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,4), plt.hist(cmy.ravel(), 256)
plt.axvline(x=0, color='c')
plt.title('Histogram'), plt.xticks([]), plt.yticks([])

plt.show()