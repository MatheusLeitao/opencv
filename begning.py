import cv2 as cv

# img = cv.imread('/home/korn/6e2b3e59-8e70-47d2-bcf7-4aefd20def56.png')

capture = cv.VideoCapture(0)

def resize():
    pass

while True:
    isTrue, frame = capture.read()
    cv.imshow('Humilliation', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()