import requests
URL = "https://bdpy1027-88e92-default-rtdb.asia-southeast1.firebasedatabase.app/%s.json"

payload1 = "Hello World!"
response1 = requests.put(URL %"demo1",json=payload1)
print(response1.status_code,response1.json())

payload2 = "適用中文!"
response2 = requests.put(URL %"demo2",json=payload2)
print(response2.status_code,response2.json())

payload3 = ['Sunday','Monday',3.1415926,500,None,'週六']
response3 = requests.put(URL %"demo3",json=payload3)
print(response3.status_code,response3.json())

payload4 = {"name":"BDPY","duration":35,"instructor":"Ho"}
response4 = requests.put(URL %"demo4",json=payload4)
print(response4.status_code,response4.json())