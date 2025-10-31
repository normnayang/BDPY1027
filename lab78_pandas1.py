import pandas as pd

series1 = pd.Series([3,1,4,5,9,-2,8])
print(type(series1))
print(series1)
print(series1.values)
print(series1.index)

series2 = pd.Series([4,7,-5,3],index=['nangang','taipei','banqiao','taoyuan'])
print(series2)
print(series2.values)
print(series2.index)

print(series1[0],series1[1],series1[2])
print(series2['nangang'],series2['banqiao'],series2['taoyuan'])

print(series1[[0,1,3]])