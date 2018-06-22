#!/usr/bin/python

import  cv2

#  to start web or external web camera 
capture=cv2.VideoCapture(0)


if  capture.isOpened()  :
	print  "camera is ready to take picture"
#       current camera data ,  after frame take camera status 
	frame,status=capture.read()
	cv2.imshow("framm1",frame)
	cv2.waitKey(0)
	capture.release()
else :
	print  "check your camera drivers with OS"


