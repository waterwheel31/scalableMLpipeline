# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Add code to load in the data.
dataPath = 'census_clean.csv'
data = pd.read_csv(dataPath)

print(data)

def process_data(inputData, categorical_features, label, training=True, encoder=None, lb=None): 

    y = inputData[label]
    X = inputData.loc[:, inputData.columns != label]

    print(y)
    print(X)

    if encoder is None:
        encoder = {}
        for feature in categorical_features:
            enco = LabelEncoder()
            enco.fit(X[feature].append(pd.Series('unknown')))
            encoder[feature] = enco

    if lb is None:
        lb = LabelEncoder()
        lb.fit(y)
    
    y = lb.transform(y)

    for feature in categorical_features:
        columnData = X[feature]
        columnData = ["unknown" if x not in encoder[feature].classes_ else x for x in columnData]
        X[feature] = encoder[feature].transform(X[feature])

    print(X[:5])
    print(y[:50])

    return X, y, encoder, lb


# Optional enhancement, use K-fold cross validation instead of a train-test split.

def train():

    train, test = train_test_split(data, test_size=0.20)

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

    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    # Proces the test data with the process_data function.

    X_test, y_test, encoder, lb = process_data(
        test, categorical_features=cat_features, label="salary", training=False,\
        encoder=encoder, lb=lb
    )

    # Train and save a model.

    clf = RandomForestClassifier(max_depth=3, random_state=10)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    acc = np.sum(y_test ==  y_pred) / len(y_pred)

    print('accuracy:', acc)

    filename = 'randomForest_model.sav'
    joblib.dump(clf, filename)

    return filename, acc, y_pred


if __name__ == "__main__": 

    train()


