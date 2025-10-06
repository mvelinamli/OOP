# how to create a class

class Person:  # We define a class in Python like this: class <class_name>. It is recommended that <class_name> start with a capital letter.
    pass
    #class attributes (özellikler)
    addres = 'no information'
    #constructor (yapıcı metod)
    def __init__(self, name, year): 
        #object attributes
        self.name = name
        self.year = year
        # print('init method worked')   
        #methods (metodlar)

# objects (instances)
p1 = Person(name='veli', year=2004)   # we define a p1 object. We can access the properties and objects we defined within the Person class through the p1 object.
# print(p1)   # <__main__.Person object at 0x10251a8a0>
# print(type(p1)) # <class '__main__.Person'>

p2 = Person(name='nuri', year=2009)

#updating
p1.name = 'ahmet'
p2.year = 2035

# accessing object attributes
print(f'p1: name: {p1.name}, year: {p1.year}')
print(f'p2: name: {p2.name}, year: {p2.year}')
