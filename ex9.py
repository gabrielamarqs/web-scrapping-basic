import mechanicalsoup, time

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/dice"
page = browser.get(url)
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")

# uso do sleep 
print("i'm about to wait for five seconds")
time.sleep(5)
print("i'm done waiting")
