import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "https://www.skoob.com.br/login/"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[2] # indice do form onde está o formulario de login
form.select("input")[0]["value"] = "" # email
form.select("input")[1]["value"] = "" # senha

# 3
profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)