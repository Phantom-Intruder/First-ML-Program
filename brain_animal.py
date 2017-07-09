import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#read data
dataframe = pd.read_fwf('brain_animal.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train model on data
body_reg = KNeighborsClassifier(n_neighbors=3)
body_reg.fit(x_values, y_values.values.ravel())

while True:
	print "Enter data:",
	data = raw_input()
	print(body_reg.predict(data))