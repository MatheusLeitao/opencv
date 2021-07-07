import cv2 as cv

img = cv.imread('./images/hackerwoman.jpg')
cv.imshow('Normal image', img)

## Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Scale Image', gray)

# # Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge Cascade, there are many
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# ## Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# ## Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# ## Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# ## Cropping
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)


cv.waitKey(0)
