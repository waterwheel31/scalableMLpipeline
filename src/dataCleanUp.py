import pandas as pd 

dataPath = 'census.csv'
savePath = 'census_clean.csv'

data = pd.read_csv(dataPath)

newData = data.copy()
newData.columns = [column.strip() for column in data.columns]

print(data.columns)
print(newData.columns)

newData.to_csv(savePath, index=False)