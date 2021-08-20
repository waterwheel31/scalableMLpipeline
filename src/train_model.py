

# Script to train machine learning model.

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Add the necessary imports for the starter code.
import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Add code to load in the data.
#
dataPath = 'census_clean.csv'
data = pd.read_csv(dataPath)

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

def process_data(inputData, categorical_features, label, training=True, process_y=True): 

    if process_y:
        y = inputData[label]
    X = inputData.loc[:, inputData.columns != label]

    print('X:')
    print(X)

    X_encoders = None
    y_encoder = None

    if training:
        X_encoders = {}
        for feature in categorical_features:
            enco = LabelEncoder()
            enco.fit(X[feature].append(pd.Series('unknown')))
            X_encoders[feature] = enco

        y_encoder = LabelEncoder()
        if process_y: y_encoder.fit(y)

        joblib.dump(X_encoders, './encoders/X_encoders.joblib')
        joblib.dump(y_encoder, './encoders/y_encoder.joblib')
    
    else: 
        X_encoders = joblib.load('./encoders/X_encoders.joblib')
        if process_y: y_encoder = joblib.load('./encoders/y_encoder.joblib')

    if process_y: y = y_encoder.transform(y)

    for feature in categorical_features:
        columnData = X[feature]
        columnData = ["unknown" if x not in X_encoders[feature].classes_ else x for x in columnData]
        X[feature] = X_encoders[feature].transform(columnData)

    if process_y: return X, y
    else: return X

# Optional enhancement, use K-fold cross validation instead of a train-test split.

def train(data):

    X_train, y_train = process_data(\
        data, categorical_features=cat_features, label="salary", training=True)

    clf = RandomForestClassifier(max_depth=3, random_state=10)
    clf.fit(X_train, y_train)

    filename = './models/randomForest_model.sav'
    joblib.dump(clf, filename)

    return clf 

def predict(clf, data):

    print(data)

    X, y = process_data(\
        data, categorical_features=cat_features, label="salary", training=False)

    y_pred = clf.predict(X)

    return y_pred

def slicePredict(data): 
    
    clf = joblib.load('./models/randomForest_model.sav')

    X = process_data(data, categorical_features=cat_features, label=None, \
        training=False, process_y=False )

    y_pred = clf.predict(X)

    return y_pred


def evaluate(data, y_pred, label='salary'):

    y_encoder = joblib.load('./encoders/y_encoder.joblib')
    y_true = data[label]
    y_true = y_encoder.transform(y_true)

    acc = accuracy_score(y_true, y_pred)
    #roc = roc_curve(y_true, y_pred)
    #areaUnderCurve = auc(roc[0], roc[1])

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    f = open('./results/slice_output.txt', 'w')
    f.write(str(acc) + '\n' +  str(precision) + '\n' + str(recall) + '\n' + str(f1))
    f.close()

    return acc, precision, recall, f1

if __name__ == "__main__": 

    train_data, test_data = train_test_split(data, test_size=0.20)
    trainedModel = train(train_data)

    y_pred = predict(trainedModel, test_data)
    acc, precision, recall, f1 = evaluate(test_data, y_pred)

    print('accuracy:', acc, 'f1:', f1) 




