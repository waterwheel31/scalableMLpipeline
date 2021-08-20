# Put the code for your API here.

from fastapi import FastAPI 
from pydantic import BaseModel, Field
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

app = FastAPI()

filename = 'randomForest_model.sav'
clf = joblib.load(filename)

'''
class singleData(BaseModel): 
    age: int
    workclass: int
    fnlgt: int
    education: int
    education_num: int = Field(alias="education-num")
    marital_status: int = Field(alias="marital-status")
    occupation: int
    relationship: int
    race: int
    sex: int
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hour_per_week: int = Field(alias="hour-per-week")
    native_country: int = Field(alias="native-country")
'''

class singleData(BaseModel): 
    age: int
    workclass: int
    fnlgt: int
    education: int
    education_num: int = Field(alias="education-num")
    marital_status: int = Field(alias="marital-status")
    occupation: int
    relationship: int
    race: int
    sex: int
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hour_per_week: int = Field(alias="hour-per-week")
    native_country: int = Field(alias="native-country")


@app.get("/")
async def welcome():
    return {"greeting": "Welcome"}


@app.post("/")
async def inference(data: singleData):

    print('data:')
    print(data.age)
    inputData = [data.age, data.workclass, data.fnlgt, \
                 data.education, data.education_num, data.marital_status,\
                 data.occupation, data.relationship, data.race, \
                 data.sex, data.capital_gain, data.capital_loss, \
                 data.hour_per_week, data.native_country
                ]
    inputData = np.array(inputData).reshape(1, -1)

    result = str(clf.predict(inputData)[0])

    print('result:', result)
    print('inference')
    return {"result": result}