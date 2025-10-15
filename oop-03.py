# Object Methods

class Person:
    
    # class attributes
    address = 'no information'

    # constructor (yapıcı metod)
    def __init__(self, name, year): # you can use any words instead of "self".
        # object attributes
        self.name = name
        self.year = year

    # instance METHODS
    def intro(self):
        print('intro working...')
        print(f'Hello there. I am '+ self.name)
    def calculate_age(self):
        print('calculate_age working...')
        print(f'My name is {self.name} and my age {2025 - self.year}')

# objects (instances)
p1 = Person(name='veli', year=2004)
p2 = Person(name='nuri', year=2009)


p1.intro()
p2.calculate_age()

