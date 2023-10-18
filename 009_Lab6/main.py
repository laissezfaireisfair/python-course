import cv2

vid = cv2.VideoCapture(1)
last_frame = None

while True:
    ret, frame = vid.read()

    if last_frame is not None:
        last_frame -= frame

        cv2.imshow('frame', last_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    last_frame = frame

vid.release()
cv2.destroyAllWindows()
