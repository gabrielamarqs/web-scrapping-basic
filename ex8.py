import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "https://www.skoob.com.br/login/"
login_page = browser.get(url)
login_html = login_page.soup

# 2
i = 0
# i=+ 1
forms = login_html.select("form")
for form in forms:  
    action = form.get("action") 
    if (action == "/login/"):
        # print("hi")
        form.select("input")[0]["value"] = "" # email
        form.select("input")[1]["value"] = "" # senha

# 3
profiles_page = browser.submit(form, login_page.url)

# se a requisição da certo, ela faz o login e a url que aparece é a que foi redirecionada
# se a requisição da errado, ela não faz o login e a url que aparece é a mesma da url de login
print(profiles_page.url)