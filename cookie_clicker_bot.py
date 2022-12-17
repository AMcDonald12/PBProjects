from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://orteil.dashnet.org/experiments/cookie/"
#add path to your chrome driver below
driver_path = Service("ADD PATH HERE")
driver = webdriver.Chrome(service=driver_path)
driver.get(URL)


game_time = True
cookie = driver.find_element(By.ID, "cookie")
clicks = 100

while game_time:
    cookie.click()
    clicks -= 1
    if clicks == 0:
        game_time = False
    while not game_time:
        store = driver.find_elements(By.CSS_SELECTOR, "#store div")
        store.reverse()
        money = driver.find_element(By.ID, "money")
        
        if int(money.text.replace(",","")) >= 1000000000:
            driver.quit()
        
        for item in store:
            try:
                item.click()
            except:
                pass
            
        clicks = 100
        game_time = True
