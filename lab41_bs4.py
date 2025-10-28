from bs4 import BeautifulSoup
import requests


URL = "https://www.python.org/"
response = requests.get(URL)
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    #print(soup.header())
    #print(soup.prettify())
    mainContent = soup.find('section',{'class':'main-content'})
    #print(mainContent)
    allHeaders = mainContent.find_all('h2')
    for header in allHeaders:
        print(header.text)
    headerBanner = soup.find('div',{'class':'header-banner'})
    allHeaders = headerBanner.find_all('h1')
    for header in allHeaders:
        print("H1",header.text)