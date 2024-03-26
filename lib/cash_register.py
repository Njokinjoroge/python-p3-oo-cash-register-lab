#!/usr/bin/env python3
price_lookup = {
    "eggs": 1.99,
    "book": 5.0,
    "tomato": 1.76,
    "Lucky Charms": 4.5,
    "Ritz Crackers": 5.0,
    "Justin's Peanut Butter Cups": 2.50,
    "macbook air": 1000,
    "apple": 0.99,
}
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += float(price) * quantity
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= float(self.total) * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self.items) > 0:
            last_item = self.items.pop()
            while last_item in self.items:
                self.items.remove(last_item)
                self.total -= price_lookup[last_item]
            self.total -= price_lookup[last_item]
            if len(self.items) == 0:
                self.total = 0