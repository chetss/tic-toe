import pandas as pd

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, columns=['a', 'b'])
df1['c'] = pd.Series([10,20,30])
df1['d'] = df1['a']+df1['b']
print(df1)
del(df1['d'])
print(df1)
df1.pop('a')
print(df1)
