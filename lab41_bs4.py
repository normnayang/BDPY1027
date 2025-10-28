from bs4 import BeautifulSoup
import requests


URL = "https://www.python.org/"
response = requests.get(URL)
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    print(soup.header())
    print(soup.prettify())