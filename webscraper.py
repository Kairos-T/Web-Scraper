import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").string
    print("Page title:", title)

    content_choice = input("Do you want to retrieve the content? (y/n): ")
    if content_choice.lower() == "y":
        content = soup.get_text()
        print("Page content:\n", content)
    else:
        print("Content retrieval skipped.")

else:
    print("Failed to retrieve page.")
