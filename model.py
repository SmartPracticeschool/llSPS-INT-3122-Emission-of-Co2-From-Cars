# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('Emission_Co2.csv')

data1 = dataset[['FUELTYPE','ENGINESIZE','CYLINDERS', 'FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','FUELCONSUMPTION_COMB_MPG','CO2EMISSIONS']]

X = data1.iloc[:, :7]


#Converting words to integer values
def convert_to_int(word):
    word_dict = {'Z':1, 'X':0}
    return word_dict[word]

X['FUELTYPE'] = X['FUELTYPE'].apply(lambda x : convert_to_int(x))

y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1, 2.4, 4,11.2,7.7,9.6,29]]))