import json
import random
import time

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def wait_for(sec=2):
    time.sleep(sec)

# Lista das palavras
randomlists_url = "https://www.randomlists.com/data/words.json"
response = requests.get(randomlists_url)
words_list = random.sample(json.loads(response.text)['data'], 60)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

#Prevenir Bugs
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Rodas versão para robos do Edge
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait_for(7)

try:
    driver.get("https://login.live.com/")
    wait_for(4)
    elem = driver.find_element(By.NAME, 'loginfmt')
    elem.clear()
    elem.send_keys("seu-email-aqui") # Coloque seu email ai
    elem.send_keys(Keys.RETURN)
    wait_for(3)
    elem1 = driver.find_element(By.NAME, 'passwd')
    elem1.clear()
    elem1.send_keys("sua-senha-aqui") # Aqui a sua senha
    elem1.send_keys(Keys.ENTER)
    wait_for(3)
    elem2 = driver.find_element(By.ID, "idSIButton9")
    elem2.send_keys(Keys.ENTER)
    wait_for(3)
    elem2 = driver.get("http://www.bing.com/search?q=Arroz")
    wait_for(3)
    elem3 = driver.find_element(By.ID, 'mHamburger')
    elem3.send_keys(Keys.ENTER)
    wait_for(3)
    elem3 = driver.find_element(By.ID, 'hb_s')
    elem3.click()
    wait_for(2)
 
except Exception as e:
    print(e)
    wait_for(4)

driver.get("http://www.bing.com/search?q=")

url_base = 'http://www.bing.com/search?q='

for num, word in enumerate(words_list):
    print('{0}. URL : {1}'.format(str(num + 1), url_base + word))
    try:
        driver.get(url_base + word)
        print('\t' + driver.find_element(By.NAME, 'q').text)

    except Exception as e1:
        print(e1)
    wait_for(1)

driver.close()

randomlists_url = "https://www.randomlists.com/data/words.json"
response = requests.get(randomlists_url)
words_list = random.sample(json.loads(response.text)['data'], 20)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

mobile_emulation = { "deviceName": "Nexus 5" }
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(service=service, options=options) 

driver.get('https://www.google.com')

wait_for(7)

try:
    driver.get("https://login.live.com/")
    wait_for(4)
    elem = driver.find_element(By.NAME, 'loginfmt')
    elem.clear()
    elem.send_keys("seu-email-aqui") # Coloque seu email ai
    elem.send_keys(Keys.RETURN)
    wait_for(4)
    elem1 = driver.find_element(By.NAME, 'passwd')
    elem1.clear()
    elem1.send_keys("sua-senha-aqui") # Aqui a sua senha
    elem1.send_keys(Keys.ENTER)
    wait_for(3)
    elem2 = driver.find_element(By.ID, "idSIButton9")
    elem2.send_keys(Keys.ENTER)
    wait_for(3)
    elem2 = driver.get("http://www.bing.com/search?q=Arroz")
    wait_for(3)
    elem3 = driver.find_element(By.ID, 'mHamburger')
    elem3.send_keys(Keys.ENTER)
    wait_for(3)
    elem3 = driver.find_element(By.ID, 'hb_s')
    elem3.click()
    wait_for(3)
 
except Exception as e:
    print(e)
    wait_for(4)


url_base = 'http://www.bing.com/search?q='

for num, word in enumerate(words_list):
    print('{0}. URL : {1}'.format(str(num + 1), url_base + word))
    try:
        driver.get(url_base + word)
        print('\t' + driver.find_element(By.NAME, 'q').text)
    except Exception as e1:
        print(e1)
    wait_for(2)
driver.close()