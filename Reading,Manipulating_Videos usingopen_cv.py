import cv2

cap = cv2.VideoCapture("C:\\Users\\user\\Desktop\\vid.mp4") #Capturing the video from desktop

 #We have to read the images(Frames) to capture the video so for that purpose we use loop
while True:
    ret,frame = cap.read() #ret is boolean value and frame is the image we have captured
    
    frame = cv2.resize(frame, (700,600)) #resizing the captured frames
    
    converting_into_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converting the video into the grayscale
    
    cv2.imshow("frame", converting_into_gray)
    
    k = cv2.waitKey(25)
    
    if k == ord("s"): #To stop the video
        break

cap.release()
cv2.destroyAllWindows()
    
    
    