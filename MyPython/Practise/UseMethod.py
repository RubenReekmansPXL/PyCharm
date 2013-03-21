__author__ = 'epq_008'
class Dog(object):
    dogCount = 0   # Class Variable (Data Attribute)

    @classmethod        # test method key words
    def getDogCount(cls):
        return Dog.dogCount

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.dogCount += 1

print Dog.getDogCount()  # prints 0
pet1 = Dog("marceau", 10)
print Dog.getDogCount()  # prints 1
pet2 = Dog("marceau", 10)
print Dog.getDogCount()  # prints 2