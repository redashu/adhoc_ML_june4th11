#!/usr/bin/env python2
import  socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.10.182",9999))
from  sklearn import  tree

'''
step 1 :  data collection  or loading data
step  2:  div --  {training data , testing data}
                   for algo ,      for user 

step 3 :   train with  classifier/regression   { algo   }

step 4 :   input  testing data that leads to predicted output  

#  data with terms  
here data know as  features 

predicted output --- lables 
'''
#  apple and orange  
#  two featues  weight , textture 
#          smooth ==  1         bumpy   === 0
features=[[120,1],[130,1],[140,0],[150,0]]

label=["apple","apple","orange","orange"]

#  calling decisionTree classifier
dsc_tree=tree.DecisionTreeClassifier()
#  training data with classification 
trained=dsc_tree.fit(features,label)
while True:
	#  recv data from client as weight 
	w_data=s.recvfrom(3)
	print  w_data
	#  recv data from client as textture 
	t_data=s.recvfrom(1)
	print  t_data
	#  predicting output 
	if  w_data[1][0]   ==  t_data[1][0] :
		output=trained.predict([[int(w_data[0]),int(t_data[0])]])
		print output
	#  sending back output to  related client  
		s.sendto(output,t_data[1])

	else :
		s.sendto("wait for your turn ",t_data[1])

		print  "wrong  input seq"










