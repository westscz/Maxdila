from random import randint
from collections import OrderedDict
from maxdila.lang import Lang

class Drug:
    def __init__(self, name):
        self.name = name
        self.price = 0.0
        self.quantity = 0

        self.min_price = 22
        self.max_price = 28

        self.price_history = None

    def __add__(self, other):
        self.price = self.price * self.quantity + other.price * other.quantity
        self.quantity += other.quantity
        return self

    def update(self):
        self.price = randint(self.min_price, self.max_price)
        self.quantity = randint(0, 50)

    def __str__(self):
        return f"{self.name} | {self.price} | {self.quantity}"

class Market():
    def __init__(self):
        self.drugs_store = OrderedDict()

    def add(self, name: str, drug: Drug):
        self.drugs_store[name] = drug

    def update(self):
        for drug in self.drugs_store.values():
            drug.update()

    def show(self):
        for drug in self.drugs_store.values():
            print(drug)

market = Market()

for drug, name in Lang.get('drugs').items():
    # print(drug, name)
    market.add(drug, Drug(name))

market.show()
market.update()
market.show()