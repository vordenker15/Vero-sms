from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from colorama import Fore
from pystyle import Write, System, Colors, Colorate, Anime
from getpass import getpass
from os import system
import random
import re


a = 1

while a == 1:
      
        rakamlar = "0123456789"
        harfler = "abcdefghijklmnopqrstuvwxyz"
        buyukharfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        isim = ""
        isim += buyukharfler[random.randint(0, 25)]
        isim += rakamlar[random.randint(0, 9)]
        isim += harfler[random.randint(0, 25)]
        isim += rakamlar[random.randint(0, 9)]
        isim += buyukharfler[random.randint(0, 25)]
        isim += rakamlar[random.randint(0, 9)]
        isim += harfler[random.randint(0, 25)]
        isim += rakamlar[random.randint(0, 9)]
        isim += buyukharfler[random.randint(0, 25)] 
        isim += rakamlar[random.randint(0, 9)]
        isim += harfler[random.randint(0, 25)]
        isim += rakamlar[random.randint(0, 9)]
        isim += buyukharfler[random.randint(0, 25)]
        isim += rakamlar[random.randint(0, 9)]
        isim += harfler[random.randint(0, 25)]
        isim += rakamlar[random.randint(0, 9)]
        
        
        email = "DonutST"
        email += harfler[random.randint(0, 25)]
        email += rakamlar[random.randint(0, 9)]
        email += buyukharfler[random.randint(0, 25)]
        email += rakamlar[random.randint(0, 9)]
        email += harfler[random.randint(0, 25)]
        email += rakamlar[random.randint(0, 9)]
        email += buyukharfler[random.randint(0, 25)]
        email += rakamlar[random.randint(0, 9)]
        email += ("@gmail.com")
        
        
        sifre = "HDA2r"
        sifre += rakamlar[random.randint(0, 9)]
        sifre += buyukharfler[random.randint(0, 25)]
        sifre += rakamlar[random.randint(0, 9)]
        sifre += harfler[random.randint(0, 25)]
        sifre += rakamlar[random.randint(0, 9)]
        sifre += buyukharfler[random.randint(0, 25)]
        sifre += rakamlar[random.randint(0, 9)]
        sifre += harfler[random.randint(0, 25)]

        
        proxy_file = "proxy_list.txt"
        with open(proxy_file, "r") as file:
                proxies = file.readlines()
        proxy_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{1,5})?\b")
        proxies = [proxy for proxy in proxies if proxy_pattern.match(proxy.strip())]
        with open(proxy_file, "w") as file:
                for proxy in proxies:
                        file.write(proxy)
        for proxy in proxies:
                proxy = proxy.strip()
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument(f"--proxy-server={proxy}")
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        try:
                driver.get("https://craftrise.com.tr")
        finally:
                driver.quit()
        
        
        driver.get("https://craftrise.com.tr/kayit")
        driver.find_element(By.CSS_SELECTOR, '[id="userName"]').send_keys(isim )
        driver.find_element(By.CSS_SELECTOR, '[id="userMail1"]').send_keys(email)
        driver.find_element(By.CSS_SELECTOR, '[id="registerPass"]').send_keys(sifre)
        driver.find_element(By.CSS_SELECTOR, '[id="registerPass2"]').send_keys(sifre)
        driver.find_element(By.CSS_SELECTOR, '[id="registerTick"]').click()
        driver.find_element(By.CSS_SELECTOR, '[onclick="onClickRegister()"]').click()
        
        file = open("Hesaplar.txt", "a", encoding='utf-8')
        file.write("\n" + isim)
        file.write(":" + sifre)
        file.write("|" + email)
        file.close()
        system("cls")
        time.sleep(1)

