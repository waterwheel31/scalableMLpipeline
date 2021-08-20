
import sys, os
from fastapi.testclient import TestClient


module_dir = os.getenv( 'MY_MODULE_PATH', default=os.getcwd() )
sys.path.append( module_dir )

from main import app

client = TestClient(app)

def test_api1():

    r = client.get("/")
    assert r.status_code == 200
    assert r.json()['greeting'] == 'Welcome'

def test_api2():

    data = {
        "age": 52,
        "workclass": "Selv-emp-not-inc",
        "fnlgt": 209642,
        "education": "Bachelors",
        "education-num": 9,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hour-per-week": 45,
        "native-country": "United-States"
    }

    r = client.post('/', json=data)

    assert r.status_code == 200
    assert r.json()['result'] == '0'

def test_api3():

    data = {
    "age": 40,
    "workclass": "State-gov",
    "fnlgt": 77516,
    "education": "Bachelors",
    "education-num": 13,
    "marital-status": "Never_married",
    "occupation": "Adm-clerical",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "capital-gain": 2174,
    "capital-loss": 0,
    "hour-per-week": 40,
    "native-country": "United-States"
    }

    r = client.post('/', json=data)

    assert r.status_code == 200
    assert r.json()['result'] == '0'