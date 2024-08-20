import pandas as pd
#series using data frames
s1 = pd.Series([0,4,8])
s2 = pd.Series([1,5,9])
s3 = pd.Series([2,6,10])
s4 = pd.Series([5,10,15])

dframe = pd.DataFrame([s1,s2,s3,s4])
#dframe =dframe.drop([0])
#print(dframe)

print(dframe)

#Add another at the bottom

#s4 = 5,10,15