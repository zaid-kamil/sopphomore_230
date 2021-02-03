import cv2                      # library import -> computer vision

webcam = cv2.VideoCapture(0)    # select a camera -> 0 means first
while True:                     # keep capturing images
    state,frame = webcam.read() # read from webcam
    cv2.imshow('Webcam window',frame)
    if cv2.waitKey(1) == 27 :   # press ecs to close camera
        print('camera stopped')
        break
webcam.release()                # stop the camera
cv2.destroyAllWindows()         # close the popup window
