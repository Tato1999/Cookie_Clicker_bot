
from selenium.webdriver.common.by import By
from find_prices import Price
import time

class Buy():
    def __init__(self):
        self.money = 0
        self.store = []
        self.id = []
        self.price = Price()
        self.forClick = ''
        pass


    # def check_new_price(self,k):
    #     self.store = k.find_elements(by=By.CSS_SELECTOR, value="#store div b")
    #     self.id = id = k.find_elements(by=By.CSS_SELECTOR, value="#store div")
    #     self.price.find_all_data(self.store, self.price.get_id(id))


    def check_avilable_item(self,n,m):
        self.money = n.find_element(by=By.ID, value="money")
        for i in range(0,len(m)):
            price_real = m[i]["price"].translate(({ord(","): None}))
            money = self.money.text
            if float(money.translate(({ord(","): None}))) >= float(price_real):
                self.forClick = n.find_element(by = By.ID, value = f"{m[i]['id']}")
                self.forClick.click()
            else:
                pass
        # self.check_new_price(n)
        