#!/usr/bin/env  python3

from  sklearn.datasets  import load_iris
from sklearn import  tree
from  sklearn.model_selection  import train_test_split
from  sklearn.metrics  import accuracy_score

#  loading  iris data
iris=load_iris()

#  NOW SPLITING  
train_iris,test_iris,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.1)

#  train_iris  and  train_target data will be using under fit method

#  calling  DecisionTree  classifier
clf=tree.DecisionTreeClassifier()
# now training  data
trained=clf.fit(train_iris,train_target)
#  test with test_iris 
output=trained.predict(test_iris)
print(output)
# actual output 
print(test_target)

# calculating  accuracy score
pct=accuracy_score(test_target,output)

print(pct)

#  exporting  graph  for decisionTree
tree.export_graphviz(clf, out_file="tree.dot", max_depth=7, feature_names=iris.feature_names, class_names=iris.target_names, filled=True,rounded=True)


