import pandas as pd
import numpy as np
### list

# data = [1,2,645,4,5]

### dict 

# key will be Index
# value will be second column
# data = {1:'a',2:'b',3:'c'}

### array

# data = np.array(['A',"2",'645','4','5'])

# ser = pd.Series(data)
ser = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (ser['e'])


