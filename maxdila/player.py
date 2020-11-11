class Bag(object):
    def __init__(self):
        self.size = 100
        self.used_size = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.life = 100
        self.cash = 198
        self.bag = Bag()
