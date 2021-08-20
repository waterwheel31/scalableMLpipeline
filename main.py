

import sys, os
from fastapi.testclient import TestClient

module_dir = os.getenv( 'MY_MODULE_PATH', default=os.getcwd() )
sys.path.append(module_dir + '\src')

from fastapi import FastAPI 
from pydantic import BaseModel, Field
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
import pandas as pd 
from src.train_model import slicePredict, predict

import os

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")

app = FastAPI()

filename = 'randomForest_model.sav'
clf = joblib.load(filename)


class singleData(BaseModel): 
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int = Field(alias="education-num")
    marital_status: str = Field(alias="marital-status")
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hour_per_week: int = Field(alias="hour-per-week")
    native_country: str = Field(alias="native-country")


@app.get("/")
async def welcome():
    return {"greeting": "Welcome"}


@app.post("/")
async def inference(data: singleData):

    tempData = data.dict(by_alias=True)
  
    columns = tempData.keys()
    values = tempData.values()

    inputData = pd.DataFrame(columns=columns)
    inputData.loc[0] = values

    result = str(slicePredict(inputData)[0].tolist())

    print('result:', result)
    print('inference')
    return {"result": result}