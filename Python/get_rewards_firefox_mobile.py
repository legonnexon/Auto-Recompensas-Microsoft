import json
import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def wait_for(sec=2):
    time.sleep(sec)

randomlists_url = "https://www.randomlists.com/data/words.json"
response = requests.get(randomlists_url)
words_list = random.sample(json.loads(response.text)['data'], 20)
print('{0} words selected from {1}'.format(len(words_list), randomlists_url))

options = FirefoxOptions()

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/1SA372 Safari/604.1"
options.set_preference("general.useragent.override", user_agent)

driver = webdriver.Firefox(options=options)

wait_for(15)

try:
    driver.get("https://login.live.com/")
    wait_for(7)
    elem = driver.find_element(By.NAME, 'loginfmt')
    elem.clear()
    elem.send_keys("seu-email-aqui") # Coloque seu email ai
    elem.send_keys(Keys.RETURN)
    wait_for(5)
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
        print('\t' + driver.find_element(By.NAME, 'h2').text)
    except Exception as e1:
        print(e1)
    wait_for(2)
driver.close()