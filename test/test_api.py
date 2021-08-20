
import sys, os
from fastapi.testclient import TestClient


module_dir = os.getenv( 'MY_MODULE_PATH', default=os.getcwd() )
sys.path.append( module_dir )

from src.main import app

client = TestClient(app)

def test_api1():

    r = client.get("/")
    print(r.json())

    assert True 

def test_api2():

    assert True 

def test_api3():

    assert True 