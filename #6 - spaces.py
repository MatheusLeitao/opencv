import cv2 as cv
# import matplotlib.pyplot as plt

img = cv.imread('./images/hackerwoman.jpg')
cv.imshow('Normal image', img)

# plt.imshow(img)
# plt.show()

"""
* All of its functions works the otherway around!
!you CANNOT convert Gray, HSV, LAb, etc... directlye
* it must be converted from BGR first.

"""

## BGR TO GRAAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



## BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)



## BGR TO L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)


## BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

cv.waitKey(0)
cv.destroyAllWindows()