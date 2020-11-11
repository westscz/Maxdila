from pprint import pprint

class Save:
    morale_values = ['?', '?', 'słabe', 'średnie', 'dobre', 'wysokie', 'bardzo wysokie'] # 12 ?! WTF

    def get_next_int(self, open_file):
        return int(next(open_file))

    def get_next_bool(self, open_file):
        return next(open_file)[:-1] is not 'FALSE'

    def load_save(self, save_path):
        with open("/home/jarek/Projects/Maxdila/save.txt") as save_file:
            self.day_limit = self.get_next_int(save_file)
            self.flags = [self.get_next_bool(save_file) for n in range(8)]
            self.player_name = next(save_file)
            self.day = self.get_next_int(save_file)
            self.store_available = self.get_next_int(save_file)
            self.store_all = self.get_next_int(save_file)
            self.cash = self.get_next_int(save_file)
            self.deposit = self.get_next_int(save_file)
            self.debt = self.get_next_int(save_file)
            self.respect = self.get_next_int(save_file)
            self.life = self.get_next_int(save_file)
            self.undefined = next(save_file)
            self.items_name = [next(save_file) for n in range(10)]  # Gun, Kalach, Granat, Shurikan
            self.items_quantity = [next(save_file) for n in range(10)]  # Peski do gnata, magazynek, granat, shurikan
            self.undefined2 = next(save_file)
            self.gang_price = self.get_next_int(save_file)
            self.morale = self.get_next_int(save_file) #self.morale_values[self.get_next_int(save_file)]
            self.result = self.get_next_int(save_file)
            self.gang_name = next(save_file)
            self.drugs_name = [next(save_file) for n in range(10)]
            self.drugs_available = [next(save_file) for n in range(10)]
            self.drugs_bag_order = [next(save_file) for n in range(10)]
            self.drugs_bag_price = [next(save_file) for n in range(10)]
            self.undefined3 = [next(save_file) for n in range(10)]
            self.drugs_bag_quantity = [next(save_file) for n in range(10)]
            self.undefined4 = [next(save_file) for n in range(10)]
            self.drugs_bag_wtf = [next(save_file) for n in range(10)]
            self.grass = [self.get_next_int(save_file) for n in range(self.day)]
            self.scun = [self.get_next_int(save_file) for n in range(self.day)]
            self.hash = [self.get_next_int(save_file) for n in range(self.day)]
            self.acid = [self.get_next_int(save_file) for n in range(self.day)]
            self.extasy = [self.get_next_int(save_file) for n in range(self.day)]
            self.speed = [self.get_next_int(save_file) for n in range(self.day)]
            self.heroina = [self.get_next_int(save_file) for n in range(self.day)]
            self.cocaine = [self.get_next_int(save_file) for n in range(self.day)]
            self.brown_sugar = [self.get_next_int(save_file) for n in range(self.day)]
            self.grzybki = [self.get_next_int(save_file) for n in range(self.day)]


if __name__ == '__main__':
    s = Save()
    s.load_save("/home/jarek/Projects/Maxdila/save.txt")

#    pprint(s.__dict__)
    from statistics import median
    x = {'grass':s.grass,   # 20 - 29
    'scun':s.scun,          # 30 - 44
    'hash':s.hash,          # 20 - 29
    'acid':s.acid,          # 20 - 29
    'extasy':s.extasy,      # 15 - 21
    'speed':s.speed,        # 28 - 44
    'heroine':s.heroina,    # 40 - 59
    'coca': s.cocaine,      # 100 - 149
    'sugar':s.brown_sugar,  # 40 - 59
    'mush': s.grzybki}      # 15 - 21

    stat = {
    'grass':20, # - 29
    'scun': 30, #- 44
    'hash': 20, # - 29
    'acid': 20, # - 29
    'extasy': 15, #- 21
    'speed':28, # - 44
    'heroine':40, # - 59
    'coca': 100, # - 149
    'sugar':40, # - 59
    'mush': 15 # - 21
    }

    stat2 = {
    'grass':29,
    'scun':44,
    'hash':29,
    'acid':29,
    'extasy':21,
    'speed':44,
    'heroine':59,
    'coca': 149,
    'sugar':59,
    'mush': 21,
    }
    for name, values in x.items():
        print("="*10, name, "="*10)
        print("Min:", min(values), " Median:", median(values), " Max:",  max(values), " Sub:", max(values)-min(values))
        ep = len([x for x in values if x<stat[name]])
        em = len([x for x in values if x>stat2[name]])
        print("Event--: ", ep,"|", format((ep*100)/s.day, '.2f'), "%")
        print("Event++: ", em,"|", format((em*100)/s.day, '.2f'), "%")
        # print("All", sorted(values))



