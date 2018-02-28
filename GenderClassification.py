# https://github.com/chribsen/simple-machine-learning-examples/blob/master/very_simple_examples/k_nearest_neighbor.py

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score

import numpy as np

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], 
	 [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 
	 'male', 'female', 'female', 'female', 'male', 'male']

neigh = KNeighborsClassifier(n_neighbors=3)
reg = LogisticRegression()
gnb = GaussianNB()

neigh.fit(X, Y)
reg.fit(X, Y)
gnb.fit(X, Y)

classifiers_scores = np.array([['K Neighbors Classifier', accuracy_score(Y, neigh.predict(X))*100], 
	['Logistic Regression', accuracy_score(Y, reg.predict(X))*100], 
	['Gaussian NB', accuracy_score(Y, gnb.predict(X))*100]])

print('Classifier : Accuracy Score')
for classifier_score in classifiers_scores:
	print(classifier_score[0] + " : " + classifier_score[1]) 

print('\nBest classifier is {}'.format(classifiers_scores[np.argmax(classifiers_scores[:,1].astype(float)), 0]))
