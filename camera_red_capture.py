#!/usr/bin/python

import  cv2,time

#  reading  image
cap=cv2.VideoCapture(0)

while cap.isOpened():

	#  taking frames 
	status,frame=cap.read()
	#  extracting only  red color 
	onlyred=cv2.inRange(frame,(0,0,0),(40,40,255))
	print  onlyred
	onlygreen=cv2.inRange(frame,(0,0,0),(40,255,0))
	#cv2.imshow('onlygreen',onlygreen)

	if  cv2.waitKey(1)  &  0xFF == ord('q') :
		break 


cv2.destroyAllWindows()
cap.release()





