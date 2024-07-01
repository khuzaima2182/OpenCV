import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 0 used for the capturing of the video from webcam

#it is 4 byte code which is use to specify the video codec
#fourcc is a manager which helps Video Writer to store the video
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"

output = cv2.VideoWriter("C:\\Users\\user\\Desktop\\output.avi",fourcc,20.0,(640,480))


while cap.isOpened(): #If the value is true then cam will capture the video
    ret,frame = cap.read()
    
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converted the captured frame into the gray scale
        
        cv2.imshow("Web Cam Video", frame)
        
        output.write(frame)
        k = cv2.waitKey(1) #1 here is used for video and 0 is for image
        
        if k == ord("t"): #stopping the video using the t button from desktop
            break


cap.release()
output.release()
cv2.destroyAllWindows()
