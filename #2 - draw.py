import cv2 as cv
import numpy as np

# image = cv.imread('./images/hackerman.jpg')
# cv.imshow('Hackerman', image)

blank = np.zeros((500, 500, 3), dtype='uint8')

# 1. Paints the image partially
blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)


# 2. Draw a rectangle
# cv.rectangle(blank,(0,0), (250,250), (0,0,255), thickness=2 )
# cv.imshow('rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (350, 250), 50, (0,0,255), thickness=2 )
# cv.imshow('Circle', blank)


# 3. Draw a line
cv.line(blank, (300,200),(400,300), (0,0,255), thickness=2 )
cv.line(blank, (400,200),(300,300), (0,0,255), thickness=2 )

# 4. Write text
cv.putText(blank, 'I\'m a master', (300,185), cv.FONT_HERSHEY_TRIPLEX, .4, (0,0,255),thickness=1)
cv.imshow('Rectangle', blank)
cv.waitKey(0)