from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from find_prices import Price
from buy_extentions import Buy
import time

chrome_drive_path = "/Users/programing/Downloads/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(by=By.ID, value="cookie")

store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")

id = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")

price = Price()
price_export = price.find_all_data(store, id)

money = Buy()
error_count = 0
while True:
    cookie.click()
    # id = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    try:
        money.check_avilable_item(n = driver,m = price_export)
    except Exception as err:
        error_count += 1
        print(f"{err}:{error_count}")
    
