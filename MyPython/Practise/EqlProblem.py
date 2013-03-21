__author__ = 'epq_008'
#Equality Testing (__eq__)
#The problem
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

pet1 = Dog("marceau", 10)
pet2 = Dog("marceau", 10)
print pet1 == pet2  # prints False (but we want True!)


#The solution:  Use __eq__
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name == other.name) and (self.age == other.age)

pet1 = Dog("marceau", 10)
pet2 = Dog("marceau", 10)
print pet1 == pet2  # prints True (huzzah!)