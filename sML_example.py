#!/usr/bin/python3

from   sklearn  import  tree

#  features about  apple and orange 
#  where 0 means smooth and  1  means bumpy  
data=[[100,0],[130,0],[135,1],[150,1]] 

output=["apple","apple","orange","orange"] 

#  decision tree algo call 
algo=tree.DecisionTreeClassifier()

#  train data 
trained_algo=algo.fit(data,output)

#  now testing phase 
predict=trained_algo.predict([[126,1]])

#  printing output 
print(predict)



