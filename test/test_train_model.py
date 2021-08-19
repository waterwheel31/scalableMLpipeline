

import sys, os

module_dir = os.getenv( 'MY_MODULE_PATH', default=os.getcwd() )
sys.path.append( module_dir )

import pytest 
from src.train_model import train


def test_test1():

    filename, acc, y_pred = train()

    assert  0.0 <= acc <= 1.0  

def test_test2():

    filename, acc, y_pred = train()

    assert filename == 'randomForest_model.sav'

def test_test3():

    filename, acc, y_pred = train()

    assert len(y_pred) > 0 