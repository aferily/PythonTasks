class Animal:
    food = None

    @classmethod
    def eat(cls):
        return cls.food
    
class Bear(Animal):
    food = 'berries'

class Rabbit(Animal):
    food = 'clover'

class Octothorpe(Animal):
    food = 'campers'

bear = Bear()
print(f'bear eats {bear.eat()}')

rabbit = Rabbit()
print(f'bear eats {rabbit.eat()}')

oct = Octothorpe()
print(f'bear eats {oct.eat()}')