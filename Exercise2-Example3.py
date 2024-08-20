import pandas as pd

data = {
    "age": [42,38,39],
    "weight":[50,40,45]
}

myvar = pd.DataFrame(data)
print(myvar.loc[0])
print(myvar.loc[[0,1]])
print(myvar.loc[[0,1,2]])
