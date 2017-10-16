import cv2
from matplotlib import pyplot as plt
import os

# for get url/directory name
base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_url = os.path.join(base_url, '00_image')

# image name
image = os.path.join(image_url, 'aircraft.jpg')

# cv read image
image = cv2.imread(image)

plt.hist(image.ravel(),256,[0,256])
plt.show()

