import cv2

webcam = cv2.VideoCapture(0)
while True:
    st,frame = webcam.read()
    
    # normal image
    cv2.imshow('normal',frame)

    # gray image
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('black n white',gray)

    # other filter convert
    colorframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    cv2.imshow('colored',colorframe)
    
    if cv2.waitKey(1) == 27:
        print('stopped camera')
        break
webcam.release()
cv2.destroyAllWindows()