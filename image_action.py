#!/usr/bin/python

import  cv2
#  all functions of  cv2  that is opencv model  
#print  dir(cv2)

#  reading image
#        image name , imaeg features  
#          we can write    cv2.IMREAD_COLOR instead of 1 
#          we can write    cv2.IMREAD_BGR2GRAY instead of 0
#          we can write    cv2.IMREAD_UNCHANGE_COLOR instead of -1

img=cv2.imread("dog1.jpeg")
#  to draw a line im  dog image
#        imagedata , start point , end point , color , line width
cv2.line(img,(0,0),(100,100),(100,120,255),3)
#              
cv2.rectangle(img,(20,20),(100,100),(255,255,255),-1)
cv2.circle(img,(100,100),30,(12,45,200),-1)
#  deciding font type  
#font=cv2.FONT_HERSHEY_SIMPLEX
#  putting text in image 
#           data, text , starting point , fontype , size , color
#cv2.putText(img,"DOGGG",(10,10),font,3,(100,23,200),lineType=cv2.LINE_AA)   
cv2.imshow("lineimg",img)
cv2.imwrite("dogline.jpeg",img)
cv2.waitKey(0)












