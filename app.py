from flask import Flask
from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np


app = Flask(__name__)
try:
    model = pickle.load(open('hear_log_model.pkl', 'rb'))
except FileNotFoundError as e:
    print(e)


@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def prediction():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trtbps = int(request.form['trtbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalachh = int(request.form['thalachh'])
        exng = int(request.form['exng'])
        oldpeak = float(request.form['oldpeak'])
        slp = int(request.form['slp'])
        caa = int(request.form['caa'])
        thall = int(request.form['thall'])

        output = model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])
        res = ""
        if output==0:
            res="Risk free"
        else:
            res="Risky"
        return render_template('Prediction.html',predict_res= res)


@app.route("/result" ,  methods=['GET'])
def result():
    pass


if __name__ == "__main__":
    app.run()
