import numpy as np
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def nothing(x):
    pass

cv2.namedWindow("Color Adjustments")
cv2.createTrackbar("Lower Hue", "Color Adjustments", 0, 255, nothing) #starting from 0,255 as BGR
cv2.createTrackbar("Lower Saturation", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Color Adjustments", 255, 255, nothing) #setting from 255,255 to set the initial value as 255
cv2.createTrackbar("Upper Saturation", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "Color Adjustments", 255, 255, nothing)



while cap.isOpened():
    #Capturing the video in frames
    _,frame = cap.read()
    
    #Resizing the windows 
    frame = cv2.resize(frame,(400,400))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converting the BGR or RGB into hsv
    l_h = cv2.getTrackbarPos("Lower Hue", "Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower Saturation", "Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower Value", "Color Adjustments")

    u_h = cv2.getTrackbarPos("Upper Hue", "Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper Saturation", "Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper Value", "Color Adjustments")
    
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    

    #mask is a binary mask where pixels within the specified range are set to 255 (white) and those outside the range are set to 0 (black)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    #filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Masking", mask)
    cv2.imshow("Result", res)
    
    
    cv2.imshow("res", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()