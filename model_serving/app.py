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
app = FastAPI()
pickle_in = open("diseaseFinder_dt_aug_2_2024.pkl","rb")
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
    print("hello world2")
    

   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[intArr[0], intArr[1], intArr[2],
                                      intArr[3], intArr[4], intArr[5], intArr[6],
                                      intArr[7], intArr[8], intArr[9], intArr[10], intArr[11], intArr[12], intArr[13],
                                      intArr[14], intArr[15], intArr[16], intArr[17], intArr[18], intArr[19], intArr[20]
                                      , intArr[21], intArr[22], intArr[23], intArr[24], intArr[25], intArr[26], intArr[27]
                                      , intArr[28], intArr[29], intArr[30], intArr[31], intArr[32], intArr[33], intArr[34]
                                      , intArr[35], intArr[36], intArr[37], intArr[38], intArr[39], intArr[40], 
                                      intArr[41], intArr[42], intArr[43],
                                      intArr[44], intArr[45], intArr[46], intArr[47],
                                      intArr[48], intArr[49], intArr[50], intArr[51], intArr[52], intArr[53], intArr[54],
                                      intArr[55], intArr[56], intArr[57], intArr[58], intArr[59], intArr[60], intArr[61]
                                      , intArr[62], intArr[63], intArr[64], intArr[65], intArr[66], intArr[67]
                                      , intArr[68], intArr[69], intArr[70], intArr[71], intArr[72], intArr[73], intArr[74]
                                      , intArr[75], intArr[76], intArr[77], intArr[78], intArr[79], intArr[80],
                                      intArr[81], intArr[82], intArr[83],
                                      intArr[84], intArr[85], intArr[86], intArr[87],
                                      intArr[88], intArr[89], intArr[90], intArr[91], intArr[92], intArr[93], intArr[94],
                                      intArr[95], intArr[96], intArr[97], intArr[98], intArr[99], intArr[100], intArr[101]
                                      , intArr[102], intArr[103], intArr[104], intArr[105], intArr[106], intArr[107]
                                      , intArr[108], intArr[109], intArr[110], intArr[111], intArr[112], intArr[113], intArr[114]
                                      , intArr[115], intArr[116], intArr[117], intArr[118], intArr[119], intArr[120],
                                      intArr[121], intArr[122], intArr[123], intArr[124], intArr[125]
                                      , intArr[126], intArr[127], intArr[128], intArr[129], intArr[130]]])

    return {
        'prediction': prediction.tolist()
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
    
#uvicorn app:app --reload