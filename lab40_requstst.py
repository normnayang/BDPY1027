import requests

URL = "https://bugzilla.mozilla.org/rest/bug/41"
response = requests.get(URL)
print(type(response),response.status_code)
print(response.headers)
print(response.headers['content-type'])
print(type(response.json()))
firstBug = response.json()['bugs'][0]
print(firstBug)
print(firstBug['cc_detail'])