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
pickle_in = open("diseaseFinder_dt_aug_2_2024.pkl","rb")
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
    Symptom_18=data['Symptom_18']
    Symptom_19=data['Symptom_19']
    Symptom_20=data['Symptom_20']
    Symptom_21=data['Symptom_21']
    Symptom_22=data['Symptom_22']
    Symptom_23=data['Symptom_23']
    Symptom_24=data['Symptom_24']
    Symptom_25=data['Symptom_25']
    Symptom_26=data['Symptom_26']
    Symptom_27=data['Symptom_27']
    Symptom_28=data['Symptom_28']
    Symptom_29=data['Symptom_29']
    Symptom_30=data['Symptom_30']
    Symptom_31=data['Symptom_31']
    Symptom_32=data['Symptom_32']
    Symptom_33=data['Symptom_33']
    Symptom_34=data['Symptom_34']
    Symptom_35=data['Symptom_35']
    Symptom_36=data['Symptom_36']
    Symptom_37=data['Symptom_37']
    Symptom_38=data['Symptom_38']
    Symptom_39=data['Symptom_39']
    Symptom_40=data['Symptom_40']
    Symptom_41=data['Symptom_41']
    Symptom_42=data['Symptom_42']
    Symptom_43=data['Symptom_43']
    Symptom_44=data['Symptom_44']
    Symptom_45=data['Symptom_45']
    Symptom_46=data['Symptom_46']
    Symptom_47=data['Symptom_47']
    Symptom_48=data['Symptom_48']
    Symptom_49=data['Symptom_49']
    Symptom_50=data['Symptom_50']
    Symptom_51=data['Symptom_51']
    Symptom_52=data['Symptom_52']
    Symptom_53=data['Symptom_53']
    Symptom_54=data['Symptom_54']
    Symptom_55=data['Symptom_55']
    Symptom_56=data['Symptom_56']
    Symptom_57=data['Symptom_57']
    Symptom_58=data['Symptom_58']
    Symptom_59=data['Symptom_59']
    Symptom_60=data['Symptom_60']
    Symptom_61=data['Symptom_61']
    Symptom_62=data['Symptom_62']
    Symptom_63=data['Symptom_63']
    Symptom_64=data['Symptom_64']
    Symptom_65=data['Symptom_65']
    Symptom_66=data['Symptom_66']
    Symptom_67=data['Symptom_67']
    Symptom_68=data['Symptom_68']
    Symptom_69=data['Symptom_69']
    Symptom_70=data['Symptom_70']
    Symptom_71=data['Symptom_71']
    Symptom_72=data['Symptom_72']
    Symptom_73=data['Symptom_73']
    Symptom_74=data['Symptom_74']
    Symptom_75=data['Symptom_75']
    Symptom_76=data['Symptom_76']
    Symptom_77=data['Symptom_77']
    Symptom_78=data['Symptom_78']
    Symptom_79=data['Symptom_79']
    Symptom_80=data['Symptom_80']
    Symptom_81=data['Symptom_81']
    Symptom_82=data['Symptom_82']
    Symptom_83=data['Symptom_83']
    Symptom_84=data['Symptom_84']
    Symptom_85=data['Symptom_85']
    Symptom_86=data['Symptom_86']
    Symptom_87=data['Symptom_87']
    Symptom_88=data['Symptom_88']
    Symptom_89=data['Symptom_89']
    Symptom_90=data['Symptom_90']
    Symptom_91=data['Symptom_91']
    Symptom_92=data['Symptom_92']
    Symptom_93=data['Symptom_93']
    Symptom_94=data['Symptom_94']
    Symptom_95=data['Symptom_95']
    Symptom_96=data['Symptom_96']
    Symptom_97=data['Symptom_97']
    Symptom_98=data['Symptom_98']
    Symptom_99=data['Symptom_99']
    Symptom_100=data['Symptom_100']
    Symptom_101=data['Symptom_101']
    Symptom_102=data['Symptom_102']
    Symptom_103=data['Symptom_103']
    Symptom_104=data['Symptom_104']
    Symptom_105=data['Symptom_105']
    Symptom_106=data['Symptom_106']
    Symptom_107=data['Symptom_107']
    Symptom_108=data['Symptom_108']
    Symptom_109=data['Symptom_109']    
    Symptom_110=data['Symptom_110']
    Symptom_111=data['Symptom_111']
    Symptom_112=data['Symptom_112']
    Symptom_113=data['Symptom_113']
    Symptom_114=data['Symptom_114']
    Symptom_115=data['Symptom_115']
    Symptom_116=data['Symptom_116']
    Symptom_117=data['Symptom_117']
    Symptom_118=data['Symptom_118']
    Symptom_119=data['Symptom_119']
    Symptom_120=data['Symptom_120']
    Symptom_121=data['Symptom_121']
    Symptom_122=data['Symptom_122']
    Symptom_123=data['Symptom_123']
    Symptom_124=data['Symptom_124']
    Symptom_125=data['Symptom_125']
    Symptom_126=data['Symptom_126']
    Symptom_127=data['Symptom_127']
    Symptom_128=data['Symptom_128']
    Symptom_129=data['Symptom_129']
    Symptom_130=data['Symptom_130']
    Symptom_131=data['Symptom_131']






   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[Symptom_1, Symptom_2, Symptom_3,
                                      Symptom_4, Symptom_5, Symptom_6, Symptom_7,
                                      Symptom_8, Symptom_9, Symptom_10, Symptom_11, Symptom_12,
                                      Symptom_13, Symptom_14, Symptom_15, Symptom_16, Symptom_17, 
                                      Symptom_18, Symptom_19, Symptom_20,
                                      Symptom_21, Symptom_22, Symptom_23, Symptom_24,
                                      Symptom_25, Symptom_26, Symptom_27, Symptom_28, Symptom_29,
                                      Symptom_30, Symptom_31, Symptom_32, Symptom_33, Symptom_34,
                                      Symptom_35, Symptom_36, Symptom_37,
                                      Symptom_38, Symptom_39, Symptom_40, Symptom_41,
                                      Symptom_42, Symptom_43, Symptom_44, Symptom_45, Symptom_46,
                                      Symptom_47, Symptom_48, Symptom_49, Symptom_50, Symptom_51,
                                      Symptom_52, Symptom_53, Symptom_54,
                                      Symptom_55, Symptom_56, Symptom_57, Symptom_58,
                                      Symptom_59, Symptom_60, Symptom_61, Symptom_62, Symptom_63,
                                      Symptom_64, Symptom_65, Symptom_66, Symptom_67, Symptom_68,
                                      Symptom_69, Symptom_70, Symptom_71,
                                      Symptom_72, Symptom_73, Symptom_74, Symptom_75,
                                      Symptom_76, Symptom_77, Symptom_78, Symptom_79, Symptom_80,
                                      Symptom_81, Symptom_82, Symptom_83, Symptom_84, Symptom_85,
                                      Symptom_86, Symptom_87, Symptom_88,
                                      Symptom_89, Symptom_90, Symptom_91, Symptom_92,
                                      Symptom_93, Symptom_94, Symptom_95, Symptom_96, Symptom_97,
                                      Symptom_98, Symptom_99, Symptom_100, Symptom_101, Symptom_102, 
                                      Symptom_103, Symptom_104, Symptom_105,
                                      Symptom_106, Symptom_107, Symptom_108, Symptom_109,
                                      Symptom_110, Symptom_111, Symptom_112, Symptom_113, Symptom_114,
                                      Symptom_115, Symptom_116, Symptom_117, Symptom_118, Symptom_119,
                                      Symptom_120, Symptom_121, Symptom_122,
                                      Symptom_123, Symptom_124, Symptom_125, Symptom_126,
                                      Symptom_127, Symptom_128, Symptom_129, Symptom_130, Symptom_131]])

    return {
        'prediction': prediction.tolist()
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload