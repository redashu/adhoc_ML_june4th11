#!/usr/bin/python2

import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:

	w=raw_input("enter weight of fruits in 100 to 180 range : ")
	t=raw_input("enter fruits textture 0 bumpy and 1 for smooth : ")
	s.sendto(w,("192.168.10.182",9999))
	s.sendto(t,("192.168.10.182",9999))
	print  s.recvfrom(20)


