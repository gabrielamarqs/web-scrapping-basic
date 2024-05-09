import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(10) :
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    # wait ten seconds if this isn't the last request
    if i < 3:
        print(i)
        time.sleep(10)