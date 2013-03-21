__author__ = 'epq_008'
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dogYears(self):
        return self.age*7

    def printInfo(self):
        print self.name
        print self.dogYears()


myPet = Dog("marceau", 10)
myPet.printInfo()
print myPet.__dict__