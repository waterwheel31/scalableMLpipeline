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

- accuracy:   0.83
- precision: 0.88
- recall: 0.35
- f1 score: 0.50
- (the metrics are stored in 'results/slice_output.txt')

## Ethical Considerations

- There may be some bias since people answered to the Census may not be fully representing the whole population. 

## Caveats and Recommendations

- Since Census is not conducted frequently, the data may not fully represent latest distribution.