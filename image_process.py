#!/usr/bin/python

import  cv2
#  all functions of  cv2  that is opencv model  
#print  dir(cv2)

#  reading image
#        image name , imaeg features  
#          we can write    cv2.IMREAD_COLOR instead of 1 
#          we can write    cv2.IMREAD_BGR2GRAY instead of 0
#          we can write    cv2.IMREAD_UNCHANGE_COLOR instead of -1

img=cv2.imread("dog1.jpeg",1)
img1=cv2.imread("dog1.jpeg",0)
img2=cv2.imread("dog1.jpeg",-1)
#  checking rows and cols 
print  img.shape
print img1.shape
#   to show original data of image  
print  img
#  to show images 
cv2.imshow("windowname",img)
cv2.imshow("bwimg",img1)
cv2.imshow("newok",img2)

#  save black and white  (GRAY)  image
cv2.imwrite("bac.jpeg",img1)

#  to hold  upper window  
cv2.waitKey(0)
