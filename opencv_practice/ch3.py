import cv2
import numpy as np

img = cv2.imread("2.jpeg")
print(img.shape)

imgResize = cv2.resize(img, (500,400))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("image", img)
cv2.imshow("image Resized", imgResize)
cv2.imshow("image Cropped", imgCropped)
cv2.waitKey(0)