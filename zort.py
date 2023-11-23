import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Proxy listesi içeren txt dosyasının yolunu belirtin
proxy_file = "proxy_list.txt"

# Txt dosyasındaki proxyleri okuma ve bozuk proxyleri ayıklama
with open(proxy_file, "r") as file:
    proxies = file.readlines()

# Regex deseni kullanarak proxy server:port olarak biçimlendirme
proxy_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{1,5})?\b")
proxies = [proxy for proxy in proxies if proxy_pattern.match(proxy.strip())]

# Txt dosyasındaki proxyleri silme
with open(proxy_file, "w") as file:
    for proxy in proxies:
        file.write(proxy)

# Her proxy için bir Selenium Chrome webdriveri oluşturma
for proxy in proxies:
    # Proxy server:port olarak biçimlendirme
    proxy = proxy.strip()

    # Chrome webdriver seçeneklerini ayarlama
    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server={proxy}")

    # Chrome webdriveri oluşturma ve proxy ile açma
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Proxy ile istediğiniz siteye gidin
        driver.get("http://example.com")

        # İşlem gerçekleştirme
        # ...
    finally:
        # Webdriveri kapatma
        driver.quit()




        python selenium chrome webdriverde txt dosyasındaki proxyleri kullanıp kullandıklarını ve çalışmayanları silen bir kod yazarmısın
