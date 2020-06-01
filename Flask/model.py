#Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

#Lecture du dataset
dataset = pd.read_csv('ventes.csv')

dataset['niveau'].fillna(0, inplace=True)

dataset['ventes_trim1'].fillna(dataset['ventes_trim1'].mean(), inplace=True)

X = dataset.iloc[:, :3]

#On associe les string de la première colonne à des entiers
def convert_to_int(word):
    word_dict = {'un':1, 'deux':2, 'trois':3, 'quatre':4, 'cinq':5, 'six':6, 'sept':7, 'huit':8,
                'neuf':9, 'dix':10, 'onze':11, 'douze':12, 'zero':0, 0: 0}
    return word_dict[word]

X['niveau'] = X['niveau'].apply(lambda x : convert_to_int(x))

y = dataset.iloc[:, -1]

#Récupération de l'objet pour la regression lineaire
from sklearn.linear_model import LinearRegression
regression = LinearRegression()

#On déclare notre model
model = regression.fit(X, y)

#Une solution avec pickle pour créer un dump du modèle 
#pickle.dump(regression, open('model.pkl','wb'))
#model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[4, 300, 500]]))#

#Solution Joblib de dump du modèle
from sklearn.externals import joblib
joblib_file = 'model.pkl'
joblib.dump(model, joblib_file)

#Récupération du model depuis le dump joblib
joblib_reg_model = joblib.load(joblib_file)

#On lance une prédiction sur des valeurs données
Predi = joblib_reg_model.predict([[4, 300, 500]])

