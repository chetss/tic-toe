import pandas as pd

df = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

df.to_csv('temp.csv', encoding='utf-8', index='False')
print(df)
