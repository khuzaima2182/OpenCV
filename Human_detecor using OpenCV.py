import cv2

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open a video capture (0 for default camera, or you can pass a video file path)
cap = cv2.VideoCapture("C:\\Users\\user\\Desktop\\vi.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize the frame to improve processing speed and accuracy
    frame = cv2.resize(frame, (640, 480))
    
    # Detect people in the frame
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8), padding=(16,16), scale=1.05)
    
    # Draw bounding boxes
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the output
    cv2.imshow('Human Detection', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
