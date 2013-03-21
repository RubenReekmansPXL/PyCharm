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

pet1 = Dog("marceau", 10)
pet2 = Dog("fido", 5)

print "You should not use instance.__dict__ to access"
print "instance attributes, but in theory you sure could...!"

print pet1.__dict__ # prints {'age': 10, 'name': 'marceau'}
print pet2.__dict__ # prints {'age': 5, 'name': 'fido'}