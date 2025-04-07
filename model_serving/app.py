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
from pydantic import BaseModel

# 2. Create the app object
neural_network = "diseaseFinder_neural_network_2025.pkl"
random_forest = "diseaseFinder_dt_aug_2_2024.pkl"
app = FastAPI()
pickle_in = open(neural_network,"rb")
classifier=pickle.load(pickle_in)
print("Pickle: ")
print(pickle.format_version)
print("numpy: ")
print(np.__version__)
print("Uvicorn: ")
print(uvicorn.__version__)
print("pandas: ")
print(pd.__version__)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/name')
def get_name(name: str):
    return {'Welcome To Riti Disease Finder: f{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
class SymptomInput(BaseModel):
    symptoms: str

@app.get('/predict')
def predict_disease(data: str):
    print("hello world:" + data)
    symptomsArr = data.split(',')
    print(symptomsArr)
    intArr = [int(x) for x in symptomsArr]
   
   # Ensure correct column names as per the training dataset
    column_names = [f"Symptom_{i+1}" for i in range(len(intArr))]  # Adjust indexing to match training data
   
   # Create a DataFrame with the correct feature names
    df = pd.DataFrame([intArr], columns=column_names)
   
    print("hello world2")
   
   # Make prediction using the classifier
    prediction = classifier.predict(df)
    print(prediction)
    print(df)
    prediction_array = np.array(prediction)
    predicted_class = int(np.argmax(prediction_array))
    mypredicted_list = [predicted_class]
    print("Raw probabilities:", prediction_array)
    print("Predicted class:", predicted_class)

    return {
        'prediction': mypredicted_list
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
    
#uvicorn app:app --reload