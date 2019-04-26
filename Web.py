from pprint import pprint

class Car:
    color = 'red'
    position = 0
    fuel = 0
    speed = 0
    price = 1000

    # engine_volume = 1000
    # year = 2018
    # drive = False


    def __init__(self, position, speed, fuel, color):
        self.position = position
        self.speed = speed
        self.fuel = fuel
        self.color = color

    def start(self):
        print('started')
        # self.drive = True

    def accelerate(self, value):
        self.speed += value

    def move(self, hours):
        self.position += self.speed * hours
        self.fuel -= hours * 10

    def brake(self):
        self.speed = 0

    def stop(self):
        print('stoped')
        # self.drive = False

# car = Car(100, 120, 40, 'grean')
# # car1 = Car()
#
# print(car.__dict__)
class Expensive:
    price = 10000000


class Cabrio(Car, Expensive):
    roof_status = 'folded'
    def unfold(self):
        self.roof_status = "unfold"

    def fold(self):
        self.roof_status = 'folded'
    pass

cabrio = Cabrio(100, 10, 40, 'red')

# cabrio.start()
# cabrio.unfold()
print(cabrio.price)
