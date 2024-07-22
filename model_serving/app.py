# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Symptoms import Symptom
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("diseaseFinder_dt_july_19_2024.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Riti Disease Finder: f{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_disease(data:Symptom):
    data = data.dict()
    Symptom_1=data['Symptom_1']
    Symptom_2=data['Symptom_2']
    Symptom_3=data['Symptom_3']
    Symptom_4=data['Symptom_4']
    Symptom_5=data['Symptom_5']
    Symptom_6=data['Symptom_6']
    Symptom_7=data['Symptom_7']
    Symptom_8=data['Symptom_8']
    Symptom_9=data['Symptom_9']
    Symptom_10=data['Symptom_10']
    Symptom_11=data['Symptom_11']
    Symptom_12=data['Symptom_12']
    Symptom_13=data['Symptom_13']
    Symptom_14=data['Symptom_14']
    Symptom_15=data['Symptom_15']
    Symptom_16=data['Symptom_16']
    Symptom_17=data['Symptom_17']

   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[Symptom_1, Symptom_2, Symptom_3,
                                      Symptom_4, Symptom_5, Symptom_6, Symptom_7,
                                      Symptom_8, Symptom_9, Symptom_10, Symptom_11, Symptom_12,
                                      Symptom_13, Symptom_14, Symptom_15, Symptom_16, Symptom_17]])

    return {
        'prediction': prediction.tolist()
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload