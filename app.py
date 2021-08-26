import pandas as pd
import numpy as np
import joblib
from flask import Flask ,render_templates



app = Flask(__name__)


model = joblib.load(open('model.pkl', 'rb'))

@app.route('/')

def hello():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])

def predict():
  input_values = [float(x) for x in request.form.values()]
  inp_features = [input_values]
  prediction = model.predict(inp_features)
  return render_template('home.html',output='The estimated cost of insurance is {} $'.format(prediction))
  
if __name__=='__main__':
  app.run(debug=True)
