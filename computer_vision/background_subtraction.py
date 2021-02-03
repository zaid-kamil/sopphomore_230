import cv2

bgmask = cv2.createBackgroundSubtractorMOG2()
webcam = cv2.VideoCapture(0)
while True:
    st,frame = webcam.read()
    mask = bgmask.apply(frame)
    cv2.imshow('normal',frame)
    cv2.imshow('masked video',mask)
    print(mask)
    if cv2.waitKey(1) == 27:
        print('stopped camera')
        break
webcam.release()
cv2.destroyAllWindows()