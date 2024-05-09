import mechanicalsoup


# You create a Browser instance and use it to request 
# the URL http://olympus.realpython.org/login. You 
# assign the HTML content of the page to the login_html 
# variable using the .soup property.

# 1
browser = mechanicalsoup.Browser()
base_url = "http://olympus.realpython.org"
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# login_html.select("form") returns a list of all <form> 
# elements on the page. Because the page has only one 
# <form> element, you can access the form by retrieving 
# the element at index 0 of the list. When there is only
# one form on a page, you may also use login_html.form. 
# The next two lines select the username and password 
# inputs and set their value to "zeus" and "ThunderDude",
# respectively.

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# You submit the form with browser.submit(). Notice 
# that you pass two arguments to this method, the 
# form object and the URL of the login_page, which 
# you access via login_page.url.

# 3
profiles_page = browser.submit(form, login_page.url)

# se a requisição da certo, ela faz o login e a url que aparece é a que foi redirecionada
# se a requisição da errado, ela não faz o login e a url que aparece é a mesma da url de login
# print(profiles_page.url)

links = profiles_page.soup.select("a")
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")