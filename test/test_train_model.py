import sys, os

module_dir = os.getenv( 'MY_MODULE_PATH', default=os.getcwd() )
sys.path.append( module_dir )

import pytest 
from src.train_model import train, predict, evaluate, process_data

import pandas as pd
import numpy as np
import sklearn

#
dataPath = 'census_clean.csv'
data = pd.read_csv(dataPath)


def test_test1():

    trainedModel = train(data)

    assert  isinstance(trainedModel, sklearn.ensemble.RandomForestClassifier)

def test_test2():

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X, y =  process_data(\
        data, categorical_features=cat_features, label="salary", training=False)

    assert len(X.columns) == 14

def test_test3():

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X, y =  process_data(\
        data, categorical_features=cat_features, label="salary", training=False)

    zeroOneItem = np.where((y==0) | (y==1))[0]
    
    assert len(zeroOneItem) == len(y)