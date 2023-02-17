import pickle
from flask import Flask, request, app, jsonify, url_for, render_template

import numpy as np
import pandas as pd


app = Flask(__name__)

#load the model
model = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_Data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_Data)
    print("the house price will be: ", output[0])
    return jsonify(output[0])

@app.route('/predict', methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    new_Data = scaler.transform(np.array(data).reshape(1,-1))
    output = model.predict(new_Data)
    return render_template("home.html", prediction_text = 'The predicted house price is: {}'.format(output[0]))



if __name__=="__main__":
    app.run()

