# from find_prices import Price

class Price():
    def __init__(self):
        self.sourt_price = []
        self.price_dict = {}
        self.count = 0
        self.id = []
        # self.price = Price()

    def find_all_data(self, i, k):
    #     self.id = self.price.price.get_id(id)
        for j in range(0,len(i)-1):
            self.sourt_price.append(i[j].text)
            # print(self.sourt_price)
        print(self.sourt_price)
        return self.make_dict(self.sourt_price, self.get_id(k))

    def get_id(self, n):
        for i in n:
            self.id.append(i.get_attribute("id"))
            # return i.get_attribute("id")
        return self.id
            
    
    
    def make_dict(self,n,k):
        self.sourt_price = []
        self.price_dict = {}
        count = -1
        # print(n)
        for i in n:
            count += 1
            self.count += 1
            new_list = i.split("-")

            self.price_dict[count] = {
                    "name": new_list[0],
                    "price": new_list[1],
                    "id": k[count]
                }
            new_list = []
        print(self.price_dict)
        return self.price_dict
            