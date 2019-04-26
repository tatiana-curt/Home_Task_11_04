class common:
    hunger = True
    weight_list = []

    def __init__(self, name, weight, vote):
        self.name = name
        self.weight = weight
        self.vote = vote


    def feed(self):
        self.hunger = False
        print('Вы накормили животное по имени {}. Голод = {}'.format(self.name, self.hunger))

    def summ_max_weight(self):
        common.weight_list.append(self.weight)

        global max_weight
        max_weight = max(common.weight_list)
        global summ_weigh
        summ_weigh = sum(common.weight_list)
        return max_weight
        return summ_weigh

    def get_vote(self):
        print('Животное по имени {} говорит: "{}"'.format(self.name, self.vote))

class geese(common):
    aggs = 0

    def collect_eggs(self):
       self.aggs += 1
       if self.vote == 'Га-Га':
         print('Вы собрали яйца у гуся {} - {} шт'.format(self.name, self.aggs))

class cow(common):
    # vote = 'Му-Му'
    milk = 0
    def get_milk(self):
        self.milk += 1
        if self.vote == 'Му-Му':
            print('Вы подоили корову по имени {}. У вас {} литр'.format(self.name, self.milk))

class sheep(common):
    # vote = 'Ме-Ме'
    long_wool = True
    def to_cut(self):
        self.long_wool = False
        print('Вы подстригли овцу по имени {}. Длинная шерсть = {}'.format(self.name, self.long_wool))

class chickens(geese):
    def collect_eggs(self):
        super().collect_eggs()
        if self.vote == 'Ко-Ко':
            print('Вы собрали яйца у курицы {} - {} шт'.format(self.name, self.aggs))
    # vote = 'Ко-Ко'
    pass

class goat(cow):
    def get_milk(self):
        super().get_milk()
        if self.vote == 'Бе-Бе':
            print('Вы подоили козу по имени {}. У вас {} литр'.format(self.name, self.milk))
    # vote = 'Бе-Бе'

class duck(chickens):
    def collect_eggs(self):
        super().collect_eggs()
        if self.vote == 'Кря':
            print('Вы собрали яйца у утки {} - {} шт'.format(self.name, self.aggs))
    # vote = 'Кря'



print('Работа с животными:')
animals = [['Серый', 15, 'Га-Га'],['Белый', 16, 'Га-Га'],['Ко-Ко', 5, 'Ко-Ко'],['Кукареку', 4, 'Ко-Ко'],['Манька', 45, 'Му-Му'], ['Рога', 8, 'Бе-Бе'], ['Копыта', 9, 'Бе-Бе'], ['Кряква', 9, 'Кря'], ['Барашек', 9, 'Ме-Ме'], ['Кудрявый', 9, 'Ме-Ме']]

for animals_list in animals:
    animal = common(animals_list[0], animals_list[1], animals_list[2])
    animal.feed()
    animal.summ_max_weight()
    animal.get_vote()

    if animals_list[2] == 'Га-Га' or 'Ко-Ко' or 'Кря':
        animal = duck(animals_list[0], animals_list[1], animals_list[2])
        animal.collect_eggs()
    if animals_list[2] == 'Му-Му' or 'Бе-Бе':
        animal = goat(animals_list[0], animals_list[1], animals_list[2])
        animal.get_milk()
    if animals_list[2] == 'Ме-Ме':
        animal = sheep(animals_list[0], animals_list[1], animals_list[2])
        animal.to_cut()

print('Максимальный вес = {} кг. Общий  вес животных = {} кг.'.format(max_weight, summ_weigh))
