import pandas as pd
s1 = pd.Series([0,4,8])
s2 = pd.Series([1,5,9])
s3 = pd.Series([2,6,10])
s4 = pd.Series([5,10,15])

#creating multi-dimensional table
dframe = pd.DataFrame([s1,s2,s3,s4],index =[0,1,2,3], columns =[0,1,2])
print(dframe)