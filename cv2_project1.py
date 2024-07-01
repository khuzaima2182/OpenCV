import cv2

path_of_image = input("Please enter the path --> ")

img = cv2.imread(path_of_image, 0)
img = cv2.resize(img,(560,700))
cv2.imshow("original", img)
cv2.waitKey(4000)
cv2.destroyAllWindows()