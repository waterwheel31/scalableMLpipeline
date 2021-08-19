# Put the code for your API here.

from fastapi import FastAPI 
from pydantic import BaseModel, Field
from sklearn.ensemble import RandomForestClassifier
import joblib

app = FastAPI()

filename = 'randomForest_model.sav'
clf = joblib.load(filename)

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
    result = clf.predict(data)
    print('inference')
    return {"result": result}