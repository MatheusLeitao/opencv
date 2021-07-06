import cv2 as cv

# img = cv.imread('/home/korn/6e2b3e59-8e70-47d2-bcf7-4aefd20def56.png')

capture = cv.VideoCapture(0)

def resize(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


while True:
    isTrue, frame = capture.read()
    frame_resized = resize(frame)

    cv.imshow('Humilliation', frame)
    cv.imshow('Resized Humiliation', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()