import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").string
    print("Page title:", title)
else:
    print("Failed to retrieve page")
