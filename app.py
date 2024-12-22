import pickle
from flask import Flask, request, jsonify, app, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('lr_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    transformed_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(transformed_data)
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    transformed_input = scaler.transform(np.array(data).reshape(1,-1))
    output = model.predict(transformed_input)
    return render_template('index.html', prediction_text='The predicted price of the house is {}'.format(output[0]))

if __name__ == "__main__":
    app.run(debug=True)