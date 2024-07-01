import cv2 #library for Open CV

#Loading the image
img1 = cv2.imread('C:\\Users\\user\\Desktop\\dp.jpg',1) #1 we use here is default and for colorful immage
img2 = cv2.imread('C:\\Users\\user\\Desktop\\dp.jpg',0) #0 we use here is for gray scale image
#Whereas -1 increases the saturation in images and improves the quality of read image

#Resizing the image into perfect form
img1 = cv2.resize(img1,(1280,700)) #width, height
img2 = cv2.resize(img2,(1280,700)) #width, height

img2 = cv2.flip(img2, 0) #0 used for flipping image downwards
#-1 used for flipping image downwards and changing its side

#displaying the image
cv2.imshow("original", img2)
cv2.waitKey() #Control the visualization(image) show on the screen
cv2.destroyAllWindows()
