import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit("Could not read the image.")
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, (0,0), fx=0.5, fy=0.5)

cv.imwrite('soccer_gray.png', gray)
cv.imwrite('soccer_gray_small.jpg',gray_small)

cv.imshow('Color image',img)
cv.imshow('Gray image', gray)
cv.imshow('Small Gray image', gray_small)

cv.waitKey()
cv.destroyAllWindows()