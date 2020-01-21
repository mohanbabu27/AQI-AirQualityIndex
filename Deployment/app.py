# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:09:41 2020

@author: mohan
"""
from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle

#Load the module from the disk
loaded_module=pickle.load(open('D:/ML_Practice/AQI_M/random_forest_regression_model.pkl','rb'))
app = Flask(__name__) #starting flask
@app.route('/')  #default home page
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])  #Prediction functionalisy after post fundtion
def predict():
    df=pd.read_csv('real_2018.csv')
    my_prediction=loaded_model.predict(df.iloc[:,:-1],values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',predection = my_prediction)

if __name__=='__main__':
    app.run(debug=False)

