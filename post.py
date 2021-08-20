
import requests

url = 'https://udacity-mldevops3.herokuapp.com:5000'



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

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())