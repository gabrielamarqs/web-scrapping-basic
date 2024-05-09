# beauty_soup.py

# pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
# vai parsear o html, vai tirar as tags
soup = BeautifulSoup(html, "html.parser")
# print(soup.get_text())
img_tag = soup.find_all("img")
# print(img_tag)

image1, image2 = soup.find_all("img")
# print(image2.name)

string = soup.title.string
print(string)
