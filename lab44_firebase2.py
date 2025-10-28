import requests
URL = "https://bdpy1027-88e92-default-rtdb.asia-southeast1.firebasedatabase.app/%s.json"

#payload3 = ['Sunday','Monday',3.1415926,500,None,'週六']
payload3 = {'2':'Tuesday','3':'Wednesday','4':'星期四'}
response3 = requests.patch(URL %"demo3",json=payload3)
print(response3.status_code,response3.json())

#payload4 = {"name":"BDPY","duration":35,"instructor":"Ho"}
payload4 = {'instructor':"Mark Ho","location":"Taipei"}
response4 = requests.patch(URL %"demo4",json=payload4)
print(response4.status_code,response4.json())