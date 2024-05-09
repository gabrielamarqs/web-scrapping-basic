# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
# vai parsear o html, vai tirar as tags
soup = BeautifulSoup(html, "html.parser")
profiles = soup.find_all("a")
# print(soup.a.string)
# print(profiles)
for string in profiles:
    url_profile = url+"/"+string.string
    print(url_profile.lower())
