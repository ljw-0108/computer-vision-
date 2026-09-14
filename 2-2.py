import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit("Could not read the image.")
    
cv.imshow('Display window', img)

cv.waitKey()
cv.destroyAllWindows()