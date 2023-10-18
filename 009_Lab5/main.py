import pandas as pd

dataframe = pd.DataFrame(columns=['sex', 'row_number', 'liters_drunk', 'age', 'drink', 'check_number', 'label'])

fin = open('titanic_with_labels.csv')

first_skipped = False
for line in fin.readlines():
    if not first_skipped:
        first_skipped = True
        continue
    values = line.split(',')
    dataframe.loc[dataframe.size] = values

fin.close()
