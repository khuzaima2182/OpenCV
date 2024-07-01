import numpy as np
import cv2


img = cv2.imread("C:\\Users\\user\\Desktop\\dp.jpg")

img = cv2.resize(img, (700,700))

img = cv2.line(img, (0,0), (200,200), (245,7,31), 8) #For drawing the line

img = cv2.arrowedLine(img, (0,125), (255,255), (245,7,31), 8) #for drawing arrow line

img = cv2.rectangle(img, (384,10),(510,218), (245,7,31),-1) #-1 used for filling the shape
cv2.imshow("sample", img)

cv2.waitKey(0)
cv2.destroyAllWindows()