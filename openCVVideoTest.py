import cv2
frameWidth=640
frameHeight=360

cap= cv2.VideoCapture(0) # For Web Cam

cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    sucess,img=cap.read()
    img= cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break