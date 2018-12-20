import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import numpy as np
from mlxtend.plotting import plot_learning_curves
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from sklearn import ensemble
import time
import random

    
def predict_melanomas():
        return random.randint(0,1)

def predict(data):
        df = pd.read_excel('App/heartDisease.xlsx')
        df.replace('?', -99999, inplace=True)

        X = df.ix[:, 0:13].values
        y = df.ix[:, -1].values

        for index, value in enumerate(y):
                if value>0:
                        y[index] = 1       #make all non-zero values to 1

        pca = PCA(n_components=5, whiten=True).fit(X)
        X_pca = pca.transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.5, random_state=8063)


        model = joblib.load('App/models/sam_station_heart_forest.pkl')  

        #For prediction
        # X_new = [age, sex, cp, restbp, chol, fastbs, restecg, maxhr, exang, stdepex, stslope, ca, thal]
        a = [20, 1, 2, 120,100, 0, 2, 70,1, 3, 2, 3, 3]
        data = np.asarray(data, dtype = np.float64)
        data = np.reshape(data, (1,-1))
        data = pca.transform(data)
        #X_new = pca.transform(X_new)



        prediction = model.predict(data)
        return (prediction[0])

if __name__ == "__main__":
        print (predict([20, 1, 2, 120,100, 0, 2, 70,1, 3, 2, 3, 3]))

