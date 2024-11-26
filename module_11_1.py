import pandas as pd


sep_end = '\n------------------------------------\n'
example = pd.read_csv('tmp.csv')
print(example.info(), example.shape, example.columns, sep=sep_end, end=sep_end)
example.pop('Unnamed: 0')
print(example.count(), end=sep_end)
print(example.groupby('Sex')['Age'].mean(), end=sep_end)
print(example['Sex'].value_counts(), end=sep_end)
print(example[(example['Age'] == 10) | (example['Sex'] == 'female')][['Age', 'Sex']].head(5))