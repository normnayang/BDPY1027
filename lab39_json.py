from json import loads, dumps

data1 = {'name': "Mark",'age':49,'weight': 75.0}
string1 = dumps(data1)
print(string1)

data2 = ['Sun','Mon','週二']
string2 = dumps(data2)
print(string2)


data3 = '{"name": "Mark", "age": 49, "weight": 75.0}'
data4 = '["Sun", "Mon", "\u9031\u4e8c"]'
result3 = loads(data3)
print(type(result3),result3['name'],result3['weight'])
result4 = loads(data4)
print(type(result4),result4[0],result4[1],result4[2])