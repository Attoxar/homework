import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Computer_security"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
article_text = soup.find("div", {"id": "mw-content-text"}).get_text()

print(article_text)
