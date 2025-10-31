import pandas as pd

data = {'coure':['poop','bdpy','pykt','aiocv'],
        'year':[2018,2017,2019,2020],
        'slide':[200,250,230,300]}

df1= pd.DataFrame(data)
s1 = pd.Series(['Taipei','Hsinchu','Taichung'],index=[0,1,2,3])
df1['location'] = s1
s2 = pd.Series