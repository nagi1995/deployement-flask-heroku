# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:54:24 2020

@author: Nagesh
"""

#%%


import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template

#%%

app = Flask(__name)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def predict():
    features = [x for x in request.form.values()]
    features = [np.array(features)]
    prediction = np.round(model.predict(features)[0], 2)
    
    return render_template('index.html', prediction_text = 'predicted Net hourly electrical energy is {} MW'.format(prediction))

    
if __name__ == "__main__":
    app.run(debug = True)







