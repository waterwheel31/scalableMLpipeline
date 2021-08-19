# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

- This is a model to estimate a person's salary range (<=50 K USD or 50 USD < ) from the persons attributes that come from the Census. 
- Used Random Forest classiifier from Sckit Learng

## Intended Use

- To specify focus customers 

## Training Data

- Original data comes from Cencus Data Set (https://archive.ics.uci.edu/ml/datasets/census+income)
- The whole dataset has 48,842 rows 
- Training Data is 80% of the whole dataset (randomly chosen)

## Evaluation Data

- The remaining 20% of the whole dataset 

## Metrics

- used the accuracy as the metric

## Ethical Considerations

- None 

## Caveats and Recommendations

- None 